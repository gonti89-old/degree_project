import argparse
import ConfigParser
import datetime
import os
import pymongo
import sys
import scripts.dates_prod as dates_prod
import scripts.tools as tools
from scripts.settings import prevPeriods
from scripts.settings import reports_conf
from scripts.settings import settings
from scripts.settings import country_conf


class apiReports(object):

    def __init__(self, country, report_name, date, period_type, instance_type, plan_id=None, node_id=None):
        self.country = country
        self.report_name = report_name
        self.period_type = period_type
        self.instance_type = instance_type
        self.plan_id = plan_id
        self.node_id = node_id
        self.number_of_periods = prevPeriods[self.period_type]

        self.end_date = self.convert_into_datetime(date)
        self.begin_date = dates_prod.serve_dates(self.end_date.strftime("%Y-%m-%d"),
                                                 self.period_type,
                                                 2,
                                                 self.number_of_periods)[1]
        self.current_report_conf = reports_conf[self.report_name]
        self.collections = self.current_report_conf['collections']
        self.date_args = {'begin_date': self.begin_date, 'end_date': self.end_date}

    def get_default_plan_id(self):
        return settings.get('default_plan_id')

    def get_reports_statuses(self):
        visible_reports = list()
        for name,data in reports_conf.iteritems():
            if data['isVisible']:
                visible_reports.append(name)
        statuses = [(n, "list-group-item-success") for n in visible_reports ]
        return statuses

    def set_db_connection(self):
        self.client = pymongo.MongoClient()
        self.db = self.client[self.instance_type]

    def end_db_connection(self):
        self.client.close()

    def convert_into_datetime(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%d')

    def find_plans_id(self, plans_type):
        self.set_db_connection()

        db_filters = dict()
        db_filters['country'] = self.country
        db_filters['node_id'] = country_conf[self.country]['node_id']
        db_filters['period_type'] = self.period_type
        dates = {"date": {"$gte": self.begin_date, "$lte": self.end_date}}
        db_filters.update(dates)
        db_stats = dict()
        db_stats['plan_id'] = True

        collection_name = settings['plans_type'][plans_type]['collection_name']
        available_plans = [cursor for cursor in self.db[collection_name].find(db_filters, db_stats).distinct('plan_id')]

        return available_plans

    def create_report(self):
        self.set_db_connection()
        data_to_process = list()

        for collection_name, collection_data in self.collections.iteritems():
            for collection_filter in collection_data.get('filters'):
                if getattr(self, collection_filter):
                    collection_data['filters'][collection_filter] = getattr(self, collection_filter)
                else:
                    collection_data['filters'][collection_filter] = country_conf[self.country][collection_filter]

            collection_data.update(self.date_args)

            id_visibility_status = {'_id': settings['_id']}
            collection_data['stats'].update(id_visibility_status)

            filters, stats_config = tools.prepare_query_args(collection_data, self.country, self.period_type)

            for document in self.db[collection_name].find(filters, stats_config):
                data_to_process.append(document)

        self.end_db_connection()
        function_name = self.current_report_conf["function"]
        data = eval('tools.'+function_name+'(data_to_process)')
        if not data:
            options = [str(x) for x in [self.country,
                                        self.report_name,
                                        self.end_date,
                                        self.period_type,
                                        self.instance_type,
                                        self.node_id]]

            raise ValueError('no data for ' + " ".join(options) + " choose other options"  )

        category_stat_name = self.current_report_conf['category']
        xAxis = {'categories': [str(x.strftime("%Y-%m-%d")) for x in data[category_stat_name]]}
        yAxis = {}
        title = {'text': self.current_report_conf['chart_name']}
        chart_opt = {'type': self.current_report_conf['chart_type']}
        plot_opt = self.current_report_conf['plot_options']

        series = list()
        for stat in data:
            if stat != category_stat_name:
                series.append({ 'name':stat, 'data':data[stat]})

        data_to_return = {'xAxis': xAxis,
                          'yAxis': yAxis,
                          'title': title,
                          'series': series,
                          'chart': chart_opt,
                          'plot_options': plot_opt}
        return data_to_return

if __name__ == '__main__':
    reports = apiReports(country="Poland",
                         report_name="basicStatsTrend",
                         date="2017-08-01",
                         period_type="day",
                         instance_type="prod",
                         node_id=2)
    print reports.create_report()


import sys
import datetime
from dateutil.relativedelta import relativedelta
import calendar


def serve_dates(report_date, period_type, number_of_periods, interval):
    """
    function return list of dates
    dates_production YYYY-MM-DD [number_of_periods_to_print] [what_periods[day, week, month]] [interval_between_periods]
    """
    dates = list()
    periods_map = {'month':'months', 'week':'weeks', 'day':'days', 'aggr_days':'aggr_days'}
    period_type = str(periods_map.get(period_type))
    year, month, day = parse_date(report_date)
    report_date = datetime.datetime(year, month, day)

    for iter in range(0,number_of_periods):
        if period_type == 'months':
            tmp_date = report_date-relativedelta(**{'months': (iter*int(interval))})
            last_month_day = calendar.monthrange(tmp_date.year, tmp_date.month)[1]
            tmp_date = tmp_date.replace(day=last_month_day)
        elif period_type == 'aggr_days':
            tmp_date = report_date-relativedelta(**{'months': (iter*int(interval))})
        else:
            tmp_date = report_date-relativedelta(**{period_type: (iter*int(interval))})

        dates.append(tmp_date)
    return dates

def parse_date(date):
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return year,month,day

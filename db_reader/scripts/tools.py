def prepare_query_args(data, country, period_type):
    stats_config = data['stats']
    filters = data['filters']
    dates = {"date": {"$gte": data['begin_date'], "$lte": data['end_date']}}
    filters.update(dates)
    filters.update({'country': country})
    filters.update({'period_type': period_type})

    return filters, stats_config



def basicStatsTrend(data):
    final_data = dict()
    for item in data:
        for stat, val in item.iteritems():
            if stat in final_data:
                final_data[stat].append(val)
            else:
                final_data[str(stat)] = [val]
    return final_data

def prepare_query_args(data, country, period_type):
    stats_config = data['stats']
    filters = data['filters'].copy()
    dates = {"date": {"$gte": data['begin_date'], "$lte": data['end_date']}}
    filters.update(dates)
    filters.update({'country': country})
    filters.update({'period_type': period_type})

    return filters, stats_config

def get_xAxis_configuration(chart_type, categories):
    if chart_type == "negative_stack":
        categories = [str(x) for x in categories]
        xAxis = [{
            'categories': categories,
            'reversed': 'false',
            'labels': {
                'step': 1
            }
        },
            {
            'opposite': 'true',
            'reversed': 'false',
            'categories': categories,
            'linkedTo': 0,
            'labels': {
                'step': 1
                }
            }]
    else:
        tmp = list()
        for item in categories:
            try:
                tmp.append(item.strftime("%Y-%m-%d"))
            except AttributeError:
                tmp.append(str(item))

        #xAxis = {'categories': [str(x.strftime("%Y-%m-%d"))  for x in categories]}
        xAxis = {'categories': tmp}

    return xAxis

def general(data):
    final_data = dict()
    for item in data:
        for stat, val in item.iteritems():
            if stat in final_data:
                final_data[stat].append(val)
            else:
                final_data[str(stat)] = [val]
    return final_data

def compare(data):
    data = general(data)
    values_to_inverse =  data['stat7']
    data['stat7'] = [-x for x in values_to_inverse]
    return data


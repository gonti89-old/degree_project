settings = {
    'instance_type': "prod",
    '_id': False,
    'default_platform': 'Total',
    'default_plan_id': '1',
    'plans_type':{
        'on':{
            'collection_name': 'file1'
        },
        'gem':{
            'collection_name': ''
        }
    }
}


prevPeriods = {
    'month': 12,
    'week': 52,
    'day': 31,
    'other': 12
}

country_conf = {
    'Croatia':{
        'node_id': 1,
        'plan_id': 1
    },
    'Poland':{
        'node_id': 1,
        'plan_id': 1
    }
}


reports_conf= {
    'basicStatsTrend': {
        'collections':{
            'file1':{
                'stats': {
                    'stat1': True,
                    'stat2': True,
                    'stat3': True,
                    'date':True
                },
                'filters': {
                    'node_id': 'node_id',
                    'plan_id': 'plan_id'
                }
            }
        },
        'function': 'basicStatsTrend',
        'category': 'date',
        'chart_name': 'basicStatsTrend',
        'chart_type': 'line'
    },
    'targetGroupTrend':{
        'collections':{},
        'function': 'targetGroupTrend',
        'category': 'date',
        'chart_name': 'Target Groups',
        'chart_type': 'area'

    }
}

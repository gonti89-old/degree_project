settings = {
    'instance_type': "prod",
    '_id': False,
    'default_platform': 'Total',
    'default_plan_id': '1',
    'plans_type':{
        'on':{
            'collection_name': 'universes.www'
        },
        'gem':{
            'collection_name': 'gem_stats'
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
        'study_id': 250818,
        'default_plan_id': 1
    }
}


reports_conf= {
    'basicStatsTrend': {
        'collections':{
            'universes.raw':{
                'stats': {
                    'Events': True,
                    'Sonars': True,
                    'Time': True,
                    'date':True
                },
                'filters': {
                    'NodeID': 'study_id',
                    'PlanID': 'default_plan_id'
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

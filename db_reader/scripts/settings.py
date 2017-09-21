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
    'empty':{
        'isVisible': False,
        'collections':{}
    },
    'basicStatsTrend':{
        'isVisible': True,
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
        'function': 'general',
        'category': 'date',
        'chart_name': 'basicStatsTrend',
        'chart_type': 'line',
        'plot_options': {}
    },
    'summaryTrend':{
        'isVisible': True,
        'collections':{
            'file2':{
                'stats':{
                    'stat4': True,
                    'stat5': True,
                    'stat6': True,
                    'date': True
                },
                'filters':{
                    'node_id': 'node_id',
                    'plan_id': 'plan_id'
                }
            }
        },
        'function': 'general',
        'category': 'date',
        'chart_name': 'TargetGroups',
        'chart_type': 'area',
        'plot_options':{
            'area':{
                'stacking':'normal'
            }

        }

    },
    'data_comparision':{
        'isVisible': True,
        'onePeriod': True,
        'collections':{
            'file3':{
                'stats':{
                    'stat7': True,
                    'stat8': True,
                    'name':True
                },
                'filters':{
                    'node_id': 'node_id',
                    'plan_id': 'plan_id'
                }
            }
        },
        'function': 'compare',
        'category': 'name',
        'chart_name': 'Comparison',
        'chart_type': 'bar',
        'chart_version': 'negative_stack',
        'plot_options':{
            'series':{
                'stacking':'normal'
            }

        }

    }
}

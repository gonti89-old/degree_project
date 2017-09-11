def get_instances():
    instances_list = [(x, x) for x in ['prod', 'beta']]
    return instances_list

def get_period_types():
    period_types = [(x, x) for x in ['day', 'week', 'month']]
    return period_types

def get_countries():
    countries = [(country_name, country_name) for country_name in
                 ['Polska', 'Croatia', 'Ukraine', 'Turkey']]
    return countries

def get_reports_statuses():
    statuses = [(report_name, "OK") for report_name in
                ['integrity_report', 'paren_child_report', 'gem_vs_univ',
                 'weighitng_report', 'univ_vs_traffic', 'integrity']]
    return statuses

def get_platforms():
    platforms = [(x,x) for x in [1, 3, 5]]
    return platforms
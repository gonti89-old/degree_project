import datetime

def get_instances():
    instances_list = [(x, x) for x in ['prod', 'beta']]
    return instances_list

def get_period_types():
    period_types = [(x, x) for x in ['day', 'week', 'month']]
    return period_types

def get_countries():
    countries = [(country_name, country_name) for country_name in
                 ['Poland', 'Croatia', 'Ukraine', 'Turkey']]
    return countries

def get_platforms():
    platforms = [(x,x) for x in [1, 3, 5]]
    return platforms

def parse_date(date):
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return year,month,day

def cast_to_date(date_str):
    y,m,d = parse_date(date_str)
    return datetime.date(y,m,d)
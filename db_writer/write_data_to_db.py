#!/home/kgontarz/prywatne/projekt_dyplomowy/venv/bin/python
import argparse
import ConfigParser
import datetime
import os
import pymongo
import sys
import scripts.tools as tools
#from scripts.tools import is_files_exists, get_gem_id, insert_many
from scripts.settings import settings



api_files_root_path = '/home/kgontarz/prywatne/projekt_dyplomowy/data/test_data/'

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", required=True, action="store")
    parser.add_argument("--date", required=True, type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'),
                        help="proper format is YYYY-MM-DD")
    parser.add_argument("--periodType", required=True)
    return parser

if __name__ == '__main__':
    parser = init_args()
    arguments = parser.parse_args()

    year = arguments.date.strftime('%Y')
    month = arguments.date.strftime('%m')
    day = arguments.date.strftime('%d')
    instance_type = settings['instance_type']
    current_path = os.path.join(api_files_root_path, instance_type,
                                arguments.country, arguments.periodType, year, month, day)

    gem_id = tools.get_gem_id('4')

    add_info = {"gem_id": gem_id, "country": arguments.country, "date": arguments.date,
                "period_type":arguments.periodType}
    files_list = tools.get_full_paths(current_path, settings['files_to_db_update'])
    if tools.is_files_exists(files_list):
        print "all files exists"
        for file_path in files_list:
            file_name = os.path.basename(file_path)
            data_to_insert = tools.csv_to_list_of_dict(file_path, add_info)
            print "data inserted", file_name
            tools.insert_many(file_name, data_to_insert, instance_type)


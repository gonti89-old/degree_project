import ast
import csv
import os
import pymongo
import sys

from collections import namedtuple

def get_gem_id(id):
    return id

def transform_data_types(data):
    final_data = dict()
    for k, v in data.iteritems():
        try:
            final_data.update({k: ast.literal_eval(v)})
        except (SyntaxError, ValueError):
            final_data.update({k: v})
    return final_data

def csv_to_list_of_dict(input_file, add_info):
    rows = list()
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile, delimiter="\t")
        for row in reader:
            row.update(add_info)
            row = transform_data_types(row)
            rows.append(row)
    return rows



def insert_many(collection_name, data, instance_type):
    client = pymongo.MongoClient()
    db = client[instance_type]
    db[collection_name].insert_many(data)
    client.close()

def is_files_exists(files_list):
    statuses_collection  = list()
    for file_path in files_list:
        status = os.path.isfile(file_path)
        print file_path, status
        statuses_collection.append(status)
    final_status =all(statuses_collection) # check if elements are True
    return final_status

def get_full_paths(root_path, files_list):
    full_paths = list()
    for file_name in files_list:
        file_path = os.path.join(root_path, file_name)
        full_paths.append(file_path)
    return full_paths



if __name__ == '__main__':
    pass                                                                                                                             

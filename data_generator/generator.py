import argparse
import csv
import itertools
import random
import sys
    

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', required=True)
    parser.add_argument('--outfile', required=True)
    args = parser.parse_args()
    return args

def read_template(template_file):
    random_fields = dict()
    static_fields = dict()
    with open(template_file) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            stats = {'range': row['range'],
                     'type': row['type']}

            if row['is_random'] == 'True':
                random_fields[row['column_name']] = stats
            else:
                begin, end, step = row['range'].split(":")
                stats['items'] = generate_data_list(begin, end, step, stats['type'])
                static_fields[row['column_name']] = stats

    header = sorted(static_fields.keys()) + sorted(random_fields.keys())
    data = {'header': header,
            'random': random_fields,
            'static': static_fields}
    return data

def generate_data_list(begin, end, step, type):
    assert type in ['int']
    if type == "int":
        if step != '':
            step = int(step)
        else:
            step = 1
        data = [x for x in range(int(begin),int(end), step)]

    return data

def generate_value(min, max, type):
    assert type in ['int', 'float']
    result = None
    min = float(min)
    max = float(max)
    if type == 'int':
        result = random.randint(min, max)
    if type == 'float':
        result = random.uniform(min, max)
    return result

def write_row(file_handler, data, delimiter="\t"):
    data = [str(x) for x in data]
    data.append('\n')
    file_handler.write(delimiter.join(data))

def print_data(data, outfile):
    items_to_combine = list()
    for _, stats in sorted(data['static'].iteritems()):
        items_to_combine.append(stats['items'])
    with open(outfile, 'w+') as f:
        write_row(f, data['header'])
        for i in (itertools.product(*items_to_combine)):
            row = list(i)
            for _, settings in (sorted(data['random'].iteritems())):
                min,max = settings['range'].split(":")
                random_number = generate_value(min, max, settings['type'])
                row.append(random_number)
            write_row(f, row)




if __name__ == '__main__':
    args = init_args()
    template_data = read_template(args.template)
    print_data(template_data, args.outfile)

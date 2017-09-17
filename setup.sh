#!/usr/bin/env bash

cd $(dirname $0)

month_path=data/test_data/prod/Poland/day/2017/08

function create_fake_csv(){
for day in {01..31};
    do mkdir -p $month_path/$day;
    for f in {file1,file2};
        do python data_generator/generator.py \
            --template data_generator/$f\_template \
            --outfile $month_path/$day/$f;
         done ;
    done
}

create_fake_csv
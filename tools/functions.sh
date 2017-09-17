#!/usr/bin/env bash
function create_fake_csv(){
echo "creating fake data for $month_path"
for day in {01..31};
    do mkdir -p $month_path/$day;
    for f in {file1,file2};
        do python data_generator/generator.py \
            --template data_generator/$f\_template \
            --outfile $month_path/$day/$f;
         done ;
    done
}

function configure_virtaul_enviroment(){
if [ ! -e ~/.myvirtualenv/ ]
    then
        virtualenv venv
        pip install -r requirements.txt

    fi
source venv/bin/activate
}

function write_fake_data_to_db(){
for day in {01..31}; 
    do python db_writer/write_data_to_db.py \
        --country Poland \
        --date 2017-08-$day \
        --periodType day; done
}

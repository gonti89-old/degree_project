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
pip install -r requirements.txt

}


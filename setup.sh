#!/usr/bin/env bash
 
cd $(dirname $0)

month_path=data/test_data/prod/Poland/day/2017/08

. tools/functions.sh

configure_virtaul_enviroment
create_fake_csv

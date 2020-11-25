#!/bin/bash

###################################
#删除早于十天的ES集群的索引
###################################

ip=localhost

function delete_indices() {
    comp_date=`date -d "10 day ago" +"%Y-%m-%d"`
    name=$1
    name_date=${name#*76_}
    date1="$name_date 00:00:00"
    date2="$comp_date 00:00:00"

    t1=`date -d "$date1" +%s`
    t2=`date -d "$date2" +%s`

    if [ $t1 -le $t2 ]; then
        echo "$1时间早于$comp_date，进行索引删除"
        curl -XDELETE http://$ip:9200/*$name
    fi
}

curl -s -XGET http://$ip:9200/_cat/indices | awk -F" " '{print $3}' | awk -F"-" '{print $NF}' | egrep "[0-9]*\.[0-9]*\.[0-9]*" | sort | uniq  | sed 's/\./-/g' | while read LINE
do
    delete_indices $LINE
done
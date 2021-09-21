#!/bin/bash
# declare -A在mac上报错
declare -A map=()

while read line
do
    for word in $line
    do
        #:wecho $word
        if [[ -z ${map[$word]} ]];then
            map[$word]=1
            echo $word
        else
            let map[$word]++
        fi
    done
done < words.txt

# 输出无法按降序
for key in ${!map[@]}
do
    echo $key ${map[$key]}
done

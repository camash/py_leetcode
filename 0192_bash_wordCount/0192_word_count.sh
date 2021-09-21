#!/bin/bash
cat words.txt | tr -s '[:space:]' '\n' |sort > temp_file.txt
echo "" >> temp_file.txt
TEMP_STR=""
CNT=0
cat temp_file.txt | while read line
do
    #echo ${line}
    if [ "${TEMP_STR}" = "${line}" ];then
        CNT=$(( ${CNT}+1))
    else
        # not empty str then print
        if [[ -n "${TEMP_STR}" ]];then
            printf "%s\t%d\n" "${TEMP_STR}" ${CNT}
        fi
        TEMP_STR=${line}
        CNT=1
    fi
done
#printf "%s\t%d\n" "${TEMP_STR}" ${CNT}

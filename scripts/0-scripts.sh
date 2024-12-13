#!/bin/sh

files="scripts/1-init.py";

if [ $# -eq 0 ] || (($1 < 1)) || (($1 > ${#files[@]})); then
    echo "please provide a valid step to start at, i.e. 'sh scripts/0-scripts.sh 1\n'"
else
    echo "--- running the following finance-v2 scripts, starting at $1 ---\n";
    for file in ${files};
    do
        echo ${file};
        echo
    done
    counter=1
    for file in ${files};
    do
        let counter++
        if (( $counter > $1 )); then
            echo "--- running ${file}---\n";
            python3 ${file}
            if [[ $? != 0 ]]; then
                break
            fi
        fi
    done
fi

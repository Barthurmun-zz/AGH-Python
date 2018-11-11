#!/bin/bash
recurse() {
 for i in "$1"/*;do
    if [ -d "$i" ];then
        echo "dir: $i"
        recurse "$i"
    elif [ -f "$i" ]; then
        echo "file: $i"
    fi
 done
}

description() {
echo "As argument to the function you need to pass localization from which searching will start"
echo "If you do not pass any argument function will start in your current localization"
}

if [ $# != 1 ]
then
    description
    exit 1
else
    recurse $1
    exit 1
fi

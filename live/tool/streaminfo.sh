#! /bin/bash

stream_url=$1
function usage() {
    echo "sh *.sh streamurl"
}

if [ -z $stream_url ];then
    usage
    exit 1
fi

ffmpeg -i $stream_url





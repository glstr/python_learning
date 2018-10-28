#! /bin/bash

video_path=$1
stream_url=$2

function usage() {
    echo "sh *.sh video_path stream_url"
}

if [ -z $video_path ];then
    usage
    exit 1
fi

ffmpeg -re -i $video_path -vcodec libx264 -acodec aac -f flv $stream_url 

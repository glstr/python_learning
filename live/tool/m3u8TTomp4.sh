#! /bin/bash
stream_url=$1
mp4_path=$2

ffmpeg  -i $stream_url -vcodec copy -acodec copy -absf aac_adtstoasc $mp4_path

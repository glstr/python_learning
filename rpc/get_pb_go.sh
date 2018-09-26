#! /bin/bash

file_path=$1
if [ -z $file_path ];then
    echo "param error"
    exit 1
fi

protoc --go_out=plugins=grpc:. $file_path


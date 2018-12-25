#! /bin/bash

src_path=$1
key=$2

curl -X POST http://10.100.57.125:8777/rd_tool/upload  -F "file=@$src_path" -F "key=$key"

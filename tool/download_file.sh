#! /bin/bash

key=$1
dst=$2

curl -X POST http://10.100.57.125:8777/rd_tool/download -F "key=$key" > $dst

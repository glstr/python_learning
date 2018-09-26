#! /bin/bash

file_path=$1
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. $file_path

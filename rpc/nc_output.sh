#! /bin/bash

target=$1

nc -v 10.100.57.125 8777 < $target



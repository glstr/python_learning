#! /bin/bash

hours=( 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 )

for hour in "${hours[@]}";
    do {
        new_hour="20181125$hour"
        echo $new_hour
    }
done

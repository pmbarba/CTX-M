#!/bin/bash
tail -n +2 ./Buzzard2015_data.csv |cut -d "," -f 3| sort|uniq -c | sort -r >utn2.txt

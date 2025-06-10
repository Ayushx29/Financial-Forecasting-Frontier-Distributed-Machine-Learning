#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin) 
header = next(reader)  

for row in reader:
    try:
        job = row[1]
        balance = float(row[4])
        print(f"{job}\t{balance}")
    except:
        continue 
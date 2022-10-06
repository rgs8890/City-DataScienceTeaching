#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:08:41 2022

@author: rohitguptha
"""

# =============================================================================
# print("Hello, World!")
# 
# 1 + 2 * 3
# 
# for i in range(1,10):
#     print(i)
# 
# total = 0
# for i in range(1,10):
#     total = total + i
#     print(total)
# print("Final Total: ", total)
# =============================================================================


import csv
import sys

rowcount = 0
total=0
TB = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
next(TB)
for row in csv.reader(TB):
    rowcount+= 1
    try:
        value=float(row[7])
        total += value
    except:ValueError
    
average=total/rowcount
print(average)
    
print("Rowcount =",rowcount)
    

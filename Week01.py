#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:08:41 2022

@author: rohitguptha
"""

#=============================================================================
print("hello, world!")

1 + 2 * 3

for i in range(1,10):
    print(i)

total = 0
for i in range(1,10):
    total = total + i
    print(total)
print("final total: ", total)
#=============================================================================
#Exercises-Part 1
import csv
import sys


rowcount = 0
total=0
TB = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
next(TB)
for row in csv.reader(TB):
    rowcount+= 1
    if 1990 <= int(row[5]) <= 2011:
        try:
            value=float(row[7])
            total += value
        except:ValueError
    
average=total/rowcount
print(average)
    
print("Rowcount =",rowcount+1)
    
#Yes, we observe that the average value has decreased

#=============================================================================
# =============================================================================
# import numpy as np
# 
# a = np.diag(np.array([1,2,3,4,5]))
# print(a)
# b = np.random.rand(4) #uniform in 0,1
# print(b)
# c = np.random.randn(4)
# print(c)
# 
# d = np.arange(10).reshape(5,2)
# print(d.T) #Can print the transpose of a matrix
# =============================================================================
#==============================================================================
#Exercises-Part 2
import numpy as np
import matplotlib.pyplot as plt
#Create an array of integers ranging from 5-15
a = np.arange(5,16,1)
print(a)
#Create an array of seven evenly spaced elements
b = np.linspace(0,23,7)
print(b) #linspace is used for evenly spaced numbers
#Create an array following the uniform distribution
c = np.random.uniform(-1,1, size=7)
print(c)
#Visualising the array in a histogram in matplotlib
plt.hist(c, bins = 7)
#Creating two numpy arrays and finding the euclidean distance between them
x = np.random.randint(6,size = 10,dtype=int)
y = np.random.randint(8,size = 10,dtype=int)
ed = np.linalg.norm(x - y)
print(ed)
#Linear Algebra formula numpy


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:25:29 2015

@author: Adriaan
"""
import numpy as np
import pandas, scipy.optimize
import itertools
testers = range(10,51)
oldTest = 1e7
#for i in range(3,4):
#    J = (list(itertools.combinations(testers,i)))
J = list([37,43,21,23])
j = J    
J = J[::-1]
#for j in J:
names = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols='D:AA')
data2 = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols='C')

b = data2.astype(float).as_matrix().flatten()
A = names.astype(float).as_matrix()
x,residuals,rank,s = np.linalg.lstsq(A,b)
test = np.mean(np.abs((np.dot(A,x)-b)/b))
if test < oldTest:
    print(test,j2)
    print()
    oldTest = test

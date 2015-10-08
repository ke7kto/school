# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:25:29 2015

@author: Adriaan
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas, scipy.optimize
import itertools
import multiprocessing
import ctypes

#from collections import deque
testers = range(4,51)
oldTest = 1e7
def getMinimum(j):#oldTest,jbest,
        #j = J.get()
        names = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols=j)
        data2 = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols='C')
        b = data2.astype(float).as_matrix().flatten()
        A = names.astype(float).as_matrix()
        x,residuals,rank,s = np.linalg.lstsq(A,b)
        test = np.mean(np.abs((np.dot(A,x)-b)/b))
        print(j,test,sep='\t')
if __name__ == '__main__':
    test = multiprocessing.Value(ctypes.c_double,1e7)
    jBest = multiprocessing.Array(ctypes.c_int,range(5))
    testers = range(10,51)
    oldTest = 1e7
    for i in range(3,4):
        J = (list(itertools.combinations(testers,i)))
        p = multiprocessing.Pool(4)
        p.map(getMinimum,J)
        #p = multiprocessing.Process(target=getMinimum,args=(test,jBest,q))
        #q.put(J)
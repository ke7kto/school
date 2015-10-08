# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:25:29 2015

@author: Adriaan
"""
import numpy as np
import pandas, scipy.optimize
import itertools
testers = range(4,51)
testers = [8,25,31,36,38]
oldTest = 1e7
worstInOrder =                   [39,27,28,21,7,17,23,47,50]
decreasingAccuracyWorstInOrder = [34,32,46,29,22,24,40,11,12,13,26,18,42,4,35,48,14,6,10,43,30,9,5,19,45,49,44,15,41,16,37,33]
testers = list(range(4,51))
titles = ['Name',
          'ChemID',
          'HFUS (kJ/mol)',
          'beta1',
          'alfa',
          'BOaveH',
          'EArC',
          'NArC',
          'VaveC',
          'VaveH',
          'Bal',
          'BIC0',
          'BIC1',
          'BIC2',
          'CIC0',
          'CIC1',
          'CIC2',
          'Oksol',
          'IC0','IC1','IC2','flex','shap1',
          'shap2',	'shap3','KH0','KH1','KH2','KH3'
          'ZQmaxC','ZQmaxH','nel','natom','nb',
          'nC','ndb','nH','nring','nS','IA','IB','IC',
          'Ran0','Ran1','Ran2','Ran3','DP','Dphyb','DPpc','Wien']

for wio in worstInOrder:
    testers.remove(wio)
#testers+decreasingAccuracyWorstInOrder+worstInOrder[2:]
"42 breaks 13 percent error"
"30 breaks 14 percent error"
"45 breaks 15 percent error"
"44 breaks 16 percent error"
"41 breaks 18 percent error"
"20 breaks 20 percent error"
"37 breaks 23 percent error"
i = len(testers)
J = (list(itertools.combinations(testers,i)))    
J = J[::-1]
oj = []
for j in J:
    j2=j
    names = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols=j2)
    data2 = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols='C')

    b = data2.astype(float).as_matrix().flatten()
    A = names.astype(float).as_matrix()
    x,residuals,rank,s = np.linalg.lstsq(A,b)
    test = np.mean(np.abs((np.dot(A,x)-b)/b))
    if test < oldTest:
        oldTest = test
        oj = j
data2 = pandas.read_excel('QSPR database for mercaptans and sulfides.xlsx',skiprows=1,parse_cols='B')

def output(x,j):
    print("each coefficient is linear with respect to Hsub")
    for i in range(len(x)):
        print('{} = {:.2f}'.format(titles[j[i]-1],x[i]))
output(x,oj)
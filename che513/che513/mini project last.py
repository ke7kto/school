
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:08:42 2015

@author: Adriaan
"""
import matplotlib.pyplot as plt
import pandas,scipy.optimize
plt.close("all")
names = pandas.read_excel('J:\\mini project2.xlsx',skiprows=2,parse_cols='A')
names = names.as_matrix().flatten()
data = pandas.read_excel('J:\\mini project2.xlsx',skiprows=2,parse_cols='B:F')
A = data.astype(float).as_matrix()
data2 = pandas.read_excel('J:\\mini project2.xlsx',skiprows=2,parse_cols='G')
b = data2.astype(float).as_matrix()
x,residuals,rank,s = np.linalg.lstsq(A,b)
b=b.flatten()
def lModel(CH):
    return (A[:,0]*CH[0]+A[:,1]*CH[1]+A[:,2]*CH[2]+A[:,3]*CH[3]+A[:,4]*CH[4])
def nlnModel(A,CH0,CH1,CH2,CH3,CH4):
    #return A[:,0]*CH0+A[:,1]*CH1+A[:,2]*CH2+A[:,3]*CH3#+A[:,4]*CH4
    return (A.T[0]*CH0+A.T[1]*CH1+A.T[2]*CH2+A.T[3]*CH3+A.T[4]*CH4)
def longModel(A,CH0,CH1,CH2,CH3,CH4,it):
    a=2
    return A.T[0]*CH0+A.T[1]*CH1+A.T[2]*CH2+A.T[3]*CH3+A.T[4]*CH4+it*np.exp(-A.T[2])
    

popt,pcov = scipy.optimize.curve_fit(nlnModel,A,b)
poptLog,pcovLog = scipy.optimize.curve_fit(longModel,A,b)
#plt.plot(nlnModel(A,popt[0],popt[1],popt[2],popt[3],popt[4])-b)
plt.figure(figsize=(15,10))
plt.plot(b,label='DIPPR')
plt.plot(nlnModel(A,*popt),'b',label='Linear Model')
plt.plot(longModel(A,*poptLog),'r',label='Extended Model')
#plt.plot(np.dot(A,x),'b',label='Least Squares Fit')
#plt.xticks(range(83))
plt.xlim([-1,83])
plt.xticks(range(83),names,rotation='vertical')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.show()
plt.figure(figsize=(15,10))
plt.plot((nlnModel(A,*popt)-b)/b*100,'b',label='Linear Model')
plt.plot((longModel(A,*poptLog)-b)/b*100,'r',label='Extended Model')
#plt.plot((np.dot(A,x).flatten()-b)/b*100,'b',label='Least Squares Fit')
plt.ylabel('% Error')
plt.xlim([-1,83])
plt.xticks(range(83),names,rotation='vertical')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.show()
string = "The heat of sublimation of {} is about {:.3g} kJ/mol"
partAlog = ['n-nonadecane',longModel(np.array([0,0,17,2,0]),*poptLog)]
partA = ['n-nonadecane',nlnModel(np.array([0,0,17,2,0]),*popt)]
partB = ['2,2-dimethyl-3,3-diethylhexane',nlnModel(np.array([2,0,4,6,0]),*popt)]
partBlog = ['2,2-dimethyl-3,3-diethylhexane',longModel(np.array([2,0,4,6,0]),*poptLog)]
print(string.format(*partAlog))
print(string.format(*partA))
print(string.format(*partB))
print(string.format(*partBlog))
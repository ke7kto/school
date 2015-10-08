# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:31:29 2015

@author: ke7kto
"""
import numpy as np
import scipy.sparse
from scipy.sparse.linalg import spsolve
N = 40
A = scipy.sparse.rand(N,N,0.9)
b = np.random.random(N)
A = A.toarray()
def linear_gs(A,b,itMax=1000,atol=1e-3):
    n,m = np.shape(A)
    nb, = np.shape(b)
    if nb != n:
        raise np.linalg.linalg.LinAlgError("A and b have different dimensions.")
    R = b.copy()
    x = b.copy()
    R[0]=100
    it = 0
    while np.linalg.norm(R)> atol:
        for i in range(n):
            R[i] = -(b[i] - (np.sum(A[i,:i]*x[:i])+np.sum(A[i,i+1:]*x[i+1:])))
            x[i]= 1/A[i,i]*R[i]
        it+=1
        if it > itMax:
            print("Bad day. Didn't converge. Here's my best guess.")
            return x
    return x

print(linear_gs(A,b))
print(np.linalg.solve(A,b))

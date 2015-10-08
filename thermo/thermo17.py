# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 09:06:38 2014

@author: ke7kto
"""

from math import exp
def frange(x,y,jump):
    while x<y:
        yield x
        x+=jump
def solve(function, xran):
    x="undefined"
    xerr=99999999
    for i in frange(xran[0],xran[1],(xran[1]-xran[0])/10000.):
        error=function(i)
        if(error<abs(xerr)):
            x=i
            xerr=error
    return x
P=80e5
A=-.4
P1sat=5e5
H=100e5
R=8.3144621
T=344
B1=-490e-6
B2=-87e-6
Vl=120e-6
phi1=B1*P/(R*T)
phi2=B2*P/(R*T)
Poynt=exp(Vl*(P-P1sat)/(R*T))
def getX(x):
    return P-x*exp(A*(1-x)**2)*P1sat*Poynt/phi1-(1-x)*H*exp(A*(x**2-1))/phi2
print solve(getX,[2.4,2.5])
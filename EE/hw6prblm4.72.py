from numpy import *
from EELaws import *
from math import *

print "\n\nProblem 72 (Amplitude, Phase)"
def toPhasorDeg(complexNum):
	return [sqrt(complexNum.real**2+complexNum.imag**2),180/pi*atan(complexNum.imag/complexNum.real)]
C=.25
L=2
R1=4
R2=4
w=2
j=complex(0,1)
Zc=-j/(w*C)
Zl=j*w*L
Ztot=series([R1,parallel([Zl,series([Zc,R2])])])
#Ztot=R1+1/(1/Zl+1/(Zc+R2))
V=2
Itot=V/Ztot
V1=V-Itot*R1
I=V1/Zl
I2=V1/(series([Zc,R2]))
print(toPhasorDeg(I))
print "\n\n"

print "Problem 74 (Amplitude, Phase)"
C=500e-6
L=.2
R1=40
R2=10
w=100
I=40
Zc=-j/(w*C)
Zl=j*w*L
A=matrix([[Zc+R1,-Zc],[-Zc,R2+Zc+Zl]])
b=matrix([[I],[0]])
Varray=linalg.solve(A,b)
print "\nV1"
print(toPhasorDeg(Varray.item(0,0)))
print "\nV2"
print(toPhasorDeg(Varray.item(1,0)))


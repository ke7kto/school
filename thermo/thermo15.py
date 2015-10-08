# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:18:54 2014

@author: ke7kto
"""
from sympy import *
from IPython.display import display
R=8.3144621
A12=1.492
A21=.956
T=298.15
y1=.6375
x1=.36
y2=1-y1
x2=1-x1
P=7
P1sat=7.9
P2sat=3.2
init_printing(use_latex='png')
gamma1=y1*P/(x1*P1sat)
gamma2=y2*P/(x2*P2sat)
from math import log
G_excess=(x1*log(gamma1)
   +x2*log(gamma2)
   +x1*log(x1)
   +x2*log(x2))*R*T
G_mix_other=(x1*x2*(A21*x1+A12*x2)+x1*log(x1)+x2*log(x2))*R*T
x=Symbol("x")
d=symbols("\Delta")
Ge=Symbol("\Delta G_E")
D2=Symbol("D_2")
c2=Symbol("c_2")
c2x=Derivative(c2,x)
Lcath=Symbol("L_{cath}")
kap2=Symbol("\kappa_2")
phi2=Symbol("\Phi_{2}")
phi2x=Derivative(phi2,x)
R=Symbol("R")
T=Symbol("T")
F=Symbol("F")
tplus=Symbol("t_{+}^0")
Activ=Symbol("\mu")
sig1=Symbol("\sigma_1")
phi1=Symbol("\Phi_1")
phi1x=Derivative(phi1,x)

Tau2=-kap2*(phi2x-2*R*T*F*(0-tplus)*Activ*c2x/c2)/Lcath
Tau1=-sig1*phi1x/Lcath
Tau0=-D2*c2x/Lcath
display(Tau0)
display(Tau1)
display(Tau2)

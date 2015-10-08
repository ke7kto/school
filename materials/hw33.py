# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 12:10:28 2014

@author: ke7kto
"""

Vf = 0.25       # fraction
d = 1e-6        # meters
l = 5e-6        # meters
sigmaf = 2.5e9  # Pascals
sigmaB = 80e6   # Pascals
lc = sigmaf*d/(2*sigmaB)
sigmaM = 10e6
if l > lc:
    stressAllowed = sigmaf*Vf*(1-lc/(2*l))+sigmaM*(1-Vf)
else:
    stressAllowed = l*sigmaB/d*Vf + sigmaM*(1-Vf)
print(stressAllowed/1e6)


Vf = 0.45       # fraction
d = 8e-6        # meters
l = 3.5e-6        # meters
sigmaf = 2.5e9  # Pascals
sigmaB = 40e6   # Pascals
lc = sigmaf*d/(2*sigmaB)
sigmaM = 12e6

stressAllowed = 1900e6
#if l > lc:
sigmaf=stressAllowed /(Vf*(1-lc/(2*l))+sigmaM*(1-Vf))
lc = sigmaf*d/(2*sigmaB)
sigmaf=stressAllowed /(Vf*(1-lc/(2*l))+sigmaM*(1-Vf))
lc = sigmaf*d/(2*sigmaB)
sigmaf=stressAllowed /(Vf*(1-lc/(2*l))+sigmaM*(1-Vf))
lc = sigmaf*d/(2*sigmaB)
sigmaf=stressAllowed /(Vf*(1-lc/(2*l))+sigmaM*(1-Vf))
lc = sigmaf*d/(2*sigmaB)
print(l>lc)
#else:
#    stressAllowed = l*sigmaB/d*Vf + sigmaM*(1-Vf)
print(sigmaf)
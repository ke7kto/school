# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 12:03:11 2014

@author: ke7kto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
ell = np.linspace(2,40)
x = 0.75

plt.plot(ell,(ell-2*x)/ell)
plt.xlabel('Length of fiber [mm]')
plt.ylabel('Reinforcement Efficiency')
plt.title('Fiber length vs Reinforcement efficiency\nAssuming x=0.75')
fig2 = plt.figure()
ax = fig2.gca(projection='3d')
print(2*x/(1-.8))
x = np.linspace(.25,1)
X,Y = np.meshgrid(x,ell)
Z = (Y-2*X)/Y
surf = ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('Length of fiber')
ax.set_zlabel('Efficiency')

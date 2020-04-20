# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:26:22 2020

@author: Jay
"""

import numpy as np
from scipy.integrate import solve_bvp
from matplotlib.pyplot import plot, show, legend, title
pi = np.pi

def f_0(x,Y):
    
    Z = np.array([Y[1],-np.exp(Y[0])])
    return Z

def bc_0(ya,yb):
    
    return np.array([ya[0] - 0,yb[0] - np.log(2)])


def f_1(x,Y):
    
    Z = np.array([Y[1],Y[1]*np.cos(x) - Y[0]*np.log(Y[0])])
    return Z

def bc_1(ya,yb):
    
    return np.array([ya[0] - 1,yb[0] - np.exp(1)])


def f_2(x,Y):
    
    Z = np.array([Y[1],-(2*Y[1]**3 + Y[1]*Y[0]**2)/np.cos(x)])
    return Z

def bc_2(ya,yb):
    
    return np.array([ya[0] - 2**(-0.25),yb[0] - (12**0.25)/2])


def f_3(x,Y):
    
    Z = np.array([Y[1],0.5 - (Y[1]**2)/2 - Y[0]*np.sin(x/2)])
    return Z

def bc_3(ya,yb):
    
    return np.array([ya[0] - 2,yb[0] - 2])


x_0 = np.linspace(1, 2, 21)
Y_0 = np.zeros((2, x_0.size))
sol_0 = solve_bvp(f_0, bc_0, x_0, Y_0)

x_1 = np.linspace(0, pi/2, 21)
Y_1 = np.full((2, x_1.size),1)
sol_1 = solve_bvp(f_1, bc_1, x_1, Y_1)

x_2 = np.linspace(pi/4, pi/3, 21)
Y_2 = np.zeros((2, x_2.size))
sol_2 = solve_bvp(f_2, bc_2, x_2, Y_2)

x_3 = np.linspace(0, pi, 21)
Y_3 = np.zeros((2, x_3.size))
sol_3 = solve_bvp(f_3, bc_3, x_3, Y_3)

plot(sol_0.x,sol_0.y[0],'r',label='solve_bvp')
title("y'' = -e^(-2y)")
legend()
show()

plot(sol_1.x,sol_1.y[0],'r',label='solve_bvp')
title(" y'' = y'cosx − ylny")
legend()
show()

plot(sol_2.x,sol_2.y[0],'r',label='solve_bvp')
title("y'' = -2(y')^3 + y'y^2")
legend()
show()

plot(sol_3.x,sol_3.y[0],'r',label='solve_bvp')
title("y'' = 1/2 - (y'^2)/2 - ysinx/2")
legend()
show()

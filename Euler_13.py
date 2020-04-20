# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:04:34 2020

@author: Jay
"""

import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

a=1
b=2
h=0.001
N=int((b-a)/h) + 1

def y_true(t):
    
    return 7*t/4 + (t**3)*np.log(t)/2 - 3*(t**3)/4

def func(Y,t):
    
    V = np.array([Y[1],2*Y[1]/t-2*Y[0]/t**2+t*np.log(t)])
    return V

t_list = np.linspace(a,b,N)
Y = np.zeros((N,2))

Y[0]=[1,0]
for i in range(N-1):

    Y[i+1] = Y[i] + h*func(Y[i],t_list[i])
 
#ode_res = odeint(func,[1,0],t_list)

plot(t_list,Y[:,0],'r',label='Euler')
#plot(t_list,ode_res[:,0],'--g',label='Odeint')
plot(t_list,y_true(t_list),'b--',label='Analytical')
title("t^2*y''-2ty'+ 2y = t^3*lnt")
legend()
show()
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:01:05 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

a=0
b=1
N=51
h=(b-a)/(N-1)

def func(Y,x):
    
    V = np.array([Y[1],2*Y[1]-Y[0]-x+x*np.exp(x)])
    return V

x_list = np.linspace(a,b,N)
Y = np.zeros((N,2))

Y[0]=[0,0]
for i in range(N-1):

    k1 = h*func(Y[i],x_list[i])
    k2 = h*func(Y[i]+k1/2,x_list[i]+h/2) 
    k3 = h*func(Y[i]+k2/2,x_list[i]+h/2)
    k4 = h*func(Y[i]+k3,x_list[i]+h)
    Y[i+1] = Y[i] + (k1+2*k2+2*k3+k4)/6
 
ode_res = odeint(func,[0,0],x_list)

plot(x_list,Y[:,0],'--r',label='RK4')
plot(x_list,ode_res[:,0],'g^',label='Odeint')
title("y''-2y'+y = xe^x - x")
legend()
show()

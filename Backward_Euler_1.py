# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:23:20 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

a=0
b=1
N=51
h=(b-a)/(N-1)

def func_1(y,x):
    
    return -9*y


def func_2(y,x):
    
    return -20*(y-x)**2 + 2*x

x_list = np.linspace(a,b,N)
v = np.zeros(N)
w = np.zeros(N)

v[0]=np.exp(1)   
for i in range(N-1):
    v[i+1] = v[i]/(1+9*h)

w[0]=1/3
for i in range(N-1):
    w[i+1] = x_list[i+1] - (1-np.sqrt(1-80*h*(x_list[i+1]-w[i])+160*h*h*x_list[i+1]))/(40*h)
    #print(1-80*h*(t_list[i+1]-w[i]))

ode_res_1 = odeint(func_1,np.exp(1),x_list)
ode_res_2 = odeint(func_2,1/3,x_list)   

plot(x_list,v,'b',label='Backward Euler')
plot(x_list,ode_res_1,'--g',label='Odeint')
title('dy/dx = -9y')
legend()
show()

plot(x_list,w,'b',label='Backward Euler')
plot(x_list,ode_res_2,'--g',label='Odeint')
title("dy/dx = -20(y-x)^2 + 2x")
legend()
show()
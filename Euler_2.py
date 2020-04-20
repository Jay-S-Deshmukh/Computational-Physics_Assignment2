# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:15:14 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

a=1
b=2
N=11
h=(b-a)/(N-1)

def f_true(t):

    return t/(1+np.log(t))

def func(y,t):

    return (y/t)*(1 - (y/t))

t_list = np.linspace(a,b,N)
v = np.zeros(N)
u = np.zeros(N)

v[0] = 1
for i in range(N-1):
    v[i+1] = v[i] + func(v[i],t_list[i])*h

for i in range(np.size(t_list)):
    u[i] = f_true(t_list[i])

ode_res = odeint(func,1,t_list)
    
plot(t_list,v,'b',label='Euler')
plot(t_list,ode_res,'--r',label='Odeint')
plot(t_list,u,'g^',label='True solution')
title('dy/dt = y/t*(1 - y/t)')
legend()
show()

abs_err = np.zeros(N)
rel_err = np.zeros(N)

for i in range(N):
    abs_err[i] = np.abs(v[i]-u[i])
    rel_err[i] = np.abs(v[i]-u[i])/u[i]

plot(t_list,abs_err,'b',label='Absolute')
plot(t_list,rel_err,'--r',label='Relative')
title("Error")
legend()
show()
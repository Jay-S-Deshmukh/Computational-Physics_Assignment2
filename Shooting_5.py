# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:37:46 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title

g=10
err=0.001

a = 0
b = 10
h = 0.01
N = int((b-a)/h) + 1

def ivp_RK4(func,X0,t_list):
    
    X = np.zeros((N,2))
    X[0]=X0
    
    for i in range(N-1):
    
        k1 = h*func(X[i],t_list[i])
        k2 = h*func(X[i]+k1/2,t_list[i]+h/2) 
        k3 = h*func(X[i]+k2/2,t_list[i]+h/2)
        k4 = h*func(X[i]+k3,t_list[i]+h)
        X[i+1] = X[i] + (k1+2*k2+2*k3+k4)/6
    
    return X
    
def f(X,t):
    
    return np.array([X[1],-g])

t_list = np.linspace(a,b,N)
z = np.zeros((N,2))
sol = np.array([z,z,z,z,z])

x_f=0
v=100
sol[0] = ivp_RK4(f, [0,v], t_list)
while(sol[0][-1,0]>(x_f+err) or sol[0][-1,0]<(x_f-err)):
    
    for i in range(4):
        sol[4-i] = sol[3-i]
    
    sol_dv = (ivp_RK4(f, [0,v+h], t_list)[-1,0] - sol[0][-1,0])/h
    v = v - (sol[0][-1,0] - x_f)/sol_dv
    sol[0] = ivp_RK4(f, [0,v], t_list)
    
plot(t_list,sol[0][:,0],'r',label='Exact sol')
plot(t_list,sol[1][:,0],'--b',label='Candidate sol')
plot(t_list,sol[2][:,0],'--b')
title('Shooting method')
legend()
show()

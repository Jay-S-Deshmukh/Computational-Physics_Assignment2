# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:31:28 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

a=0
b=1
N=21
h=(b-a)/(N-1)

def func(Y,t):
    
    v1 = Y[0] + 2*Y[1] - 2*Y[2] + np.exp(-t)
    v2 = Y[1] + Y[2] - 2*np.exp(-t)
    v3 = Y[0] + 2*Y[1] + np.exp(-t)
    
    V = np.array([v1,v2,v3])
    return V

t_list = np.linspace(a,b,N)
Y = np.zeros((N,3))


Y[0]=[3,-1,1]

for i in range(N-1):

    k1 = h*func(Y[i],t_list[i])
    k2 = h*func(Y[i]+k1/2,t_list[i]+h/2) 
    k3 = h*func(Y[i]+k2/2,t_list[i]+h/2)
    k4 = h*func(Y[i]+k3,t_list[i]+h)
    Y[i+1] = Y[i] + (k1+2*k2+2*k3+k4)/6
 
ode_res = odeint(func,[3,-1,1],t_list)

plot(t_list,Y[:,0],'r',label='u1')
plot(t_list,Y[:,1],'b',label='u2')
plot(t_list,Y[:,2],'g',label='u3')
title("RK4")
legend()
show()

plot(t_list,ode_res[:,0],'r^',label='Odeint u1')
plot(t_list,ode_res[:,1],'b^',label='Odeint u2')
plot(t_list,ode_res[:,2],'g^',label='Odeint u3')
title("Odeint")
legend()
show()
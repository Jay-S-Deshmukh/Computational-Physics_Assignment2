# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:47:45 2020

@author: Jay
"""
import numpy as np
#from matplotlib.pyplot import plot, show, legend, title
#from scipy.integrate import odeint

a=0
b=1
N1=21
h1=(b-a)/(N1-1)


def func_1(x,t):

    return 1/(x**2 + t**2)

def func_2(x,u):

    return -1/((u*x)**2 + 1)

t_list = np.linspace(a,b,N1)
x_1 = np.zeros(N1)

x_1[0]=1
for i in range(N1-1):

    k1 = h1*func_1(x_1[i],t_list[i])
    k2 = h1*func_1(x_1[i]+k1/2,t_list[i]+h1/2) 
    k3 = h1*func_1(x_1[i]+k2/2,t_list[i]+h1/2)
    k4 = h1*func_1(x_1[i]+k3,t_list[i]+h1)
    x_1[i+1] = x_1[i] + (k1+2*k2+2*k3+k4)/6

h2=0.3e-4
N2=int((b-a)/h2)
u_list = np.linspace(a,b,N2)    
x_2 = np.zeros(N2)
 
t_0 = 3.5e06
u_0 = 1/t_0

x_2[-1]=x_1[-1]
for i in reversed(range(N2)):

    k1 = h2*func_2(x_2[i],u_list[i])
    k2 = h2*func_2(x_2[i]+k1/2,u_list[i]+h2/2) 
    k3 = h2*func_2(x_2[i]+k2/2,u_list[i]+h2/2)
    k4 = h2*func_2(x_2[i]+k3,u_list[i]+h2)
    x_2[i-1] = x_2[i] - (k1+2*k2+2*k3+k4)/6
    
    if(u_list[i-1]<u_0):
        print("The value of x at t=3.5x10^6 is ",x_2[i-1])
        break
    
'''  
t_new = np.linspace(0,100,2001)
ode_res = odeint(func_1,1,t_new)
print(ode_res[-1])

plot(t_list,x_1,'--r',label='RK4')
title("dy/dt = 1/(x^2 + t^2)")
legend()
show()
'''
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:16:46 2020

@author: Jay
"""
import numpy as np
from matplotlib.pyplot import plot, show, legend, title
from scipy.integrate import odeint

def func(y,x):
    
    f = (y**2+y)/x
    return f

def RK4(y0,x0,h):
    k1 = h*func(y0,x0)
    k2 = h*func(y0+k1/2,x0+h/2) 
    k3 = h*func(y0+k2/2,x0+h/2)
    k4 = h*func(y0+k3,x0+h)
    y0 = y0 + (k1+2*k2+2*k3+k4)/6
    
    return y0

err=0.0001
h=0.1
x=[1]    
y=[-2]

i=0
while(x[i]<=3):
    
    y1 = RK4(y[i],x[i],h)
    y1 = RK4(y1,x[i]+h,h)
    y2 = RK4(y[i],x[i],2*h)
    
    h = h*np.power((err*h*30/np.abs(y2-y1)),0.25)
    y.append(RK4(y[i],x[i],h))
    x.append(x[i] + h)
    i=i+1

x_list = np.linspace(1,5,41)
ode_res = odeint(func,-2,x_list)

plot(x,y,'r^',label='Adaptive step-size')
plot(x_list,ode_res[:,0],'g',label='Odeint')
title("y' = (y^2 + y)/x")
legend()
show()

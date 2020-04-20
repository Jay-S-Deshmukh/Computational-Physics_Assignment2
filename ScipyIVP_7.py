# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:56:27 2020

@author: Jay
"""
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.pyplot import plot, show, legend, title

def f_1(t,y):
    
    return t*np.exp(3*t) - 2*y

def f_1true(t):

    return np.exp(3*t)*(t/5 -1/25) + np.exp(-2*t)/25


def f_2(t,y):
    
    return 1 - (t-y)**2

def f_2true(t):

    return t + 1/(t - 5/2)


def f_3(t,y):
    
    return 1 + y/t

def f_3true(t):

    return t*np.log(t) + 2*t


def f_4(t,y):
    
    return np.cos(2*t) + np.sin(3*t)

def f_4true(t):
    
    return np.sin(2*t)/2 - np.cos(3*t)/3 + 4/3

t_1 = t_eval=np.linspace(0,1,51)
t_2 = t_eval=np.linspace(2,3,51)
t_3 = t_eval=np.linspace(1,2,51)
t_4 = t_eval=np.linspace(0,1,51)

sol_1 = solve_ivp(f_1, [0,1], [0], t_eval=t_1)
sol_2 = solve_ivp(f_2, [2,3], [0], t_eval=t_2)
sol_3 = solve_ivp(f_3, [1,2], [2], t_eval=t_3)
sol_4 = solve_ivp(f_4, [0,1], [1], t_eval=t_4)

plot(sol_1.t,sol_1.y[0],'r',label='solve_ivp')
plot(sol_1.t,f_1true(sol_1.t),'y--',label='Analytical')
title("y' = t*e^(3t) - 2y")
legend()
show()

plot(sol_2.t,sol_2.y[0],'r',label='solve_ivp')
plot(sol_2.t,f_2true(sol_2.t),'y--',label='Analytical')
title("y' = 1 - (t-y)^2")
legend()
show()

plot(sol_3.t,sol_3.y[0],'r',label='solve_ivp')
plot(sol_3.t,f_3true(sol_3.t),'y--',label='Analytical')
title("y' = 1 + y/t")
legend()
show()

plot(sol_4.t,sol_4.y[0],'r',label='solve_ivp')
plot(sol_4.t,f_4true(sol_4.t),'y--',label='Analytical')
title("y' = cos(2t) + sin(3t)")
legend()
show()

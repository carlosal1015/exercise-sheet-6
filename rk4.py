#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:46:21 2022

@author: mehlmann
"""

import numpy as np
import matplotlib.pyplot as plt

# Implementation of the right hand side 
# x'(t) = f( x(t) )
def f(x):
    return np.array([x[1],
                     -x[0]-0.01*x[1]-100*x[2],
                     x[1]-1000.0*x[2]])


## One step of Heun's 2nd order method
def heun(x,h):
    return x+0.5*h*f(x) + 0.5*h*f(x+h*f(x))

## One step of forward Euler
def eeuler(x,h):
    return x+h*f(x)

## One step of Runge-Kutta 4
def rk4(x,h):
    k1 = f(x)
    k2 = f(x+0.5*h*k1)
    k3 = f(x+0.5*h*k2)
    k4 = f(x+h*k3)
    return x+h/6.*(k1+2.*k2+2.*k3+k4)



print('Exercise 1b)')
## Solve the problem in [0,10] and plot the solution
T = 10   # Final time
N = 6000  # Number of time steps
h = T/N  # step size

timesteps = np.linspace(0,T,N+1)  # discrete time points

x = np.zeros( (N+1,3) )           # solution vector
x[0,:] = np.array([1,1,0])        # initial solution

for i in range(N):
    x[i+1,:] = heun(x[i,:],h)
    
print('\n(i) With Heun''s method using h={0}: x(10)='.format(h),x[-1])
    
print('\n(ii) Plot the solution as graph.')
plt.title('x(t) for t in [0,10]')
plt.plot(timesteps,x,label='Heun''s solution')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

plt.title('Only w(t) for t in [0,10]')
plt.plot(timesteps,x[:,2],label='w(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()



## Determine Step sizes
print('\n(iii) Determine stable step sizes.')
print('For a sequence of step sizes we compute the solution with Explicit Euler, Heun and Runge-Kutta-4')
print('We indicate a -, when solution "explodes". We say that it "explodes" if |x(t)|>10000. ')
print('If the solution is bounded until T=10, we indicate it with a + standing for stability.')
print('')
print('h\t\t\tEuler\tHeun\t\tRK4')
for N in reversed(range(3000,6000,500)):
    h = T/N                # set step size 
    
    print('{0:2.8f}'.format(h),end='\t')
    
    ## Euler method
    x = np.array([1,1,0])  # set initial value
    stable = True
    for i in range(N):
        x = eeuler(x,h)
        if np.linalg.norm(x)>10000:
            stable = False
            break
    if stable:
        print('+',end='\t\t')
    else:
        print('-',end='\t\t')

    ## Heun's method
    x = np.array([1,1,0])  # set initial value
    stable = True
    for i in range(N):
        x = heun(x,h)
        if np.linalg.norm(x)>10000:
            stable = False
            break
    if stable:
        print('+',end='\t\t')
    else:
        print('-',end='\t\t')

    ## RK4 method
    x = np.array([1,1,0])  # set initial value
    stable = True
    for i in range(N):
        x = rk4(x,h)
        if np.linalg.norm(x)>10000:
            stable = False
            break
    if stable:
        print('+')
    else:
        print('-')

print('\n(iv) We determine the order of convergence.\n')
print('First we compute an exact solution with rk4 using h=0.0001')


exact = np.array([1,1,0])  # set initial value
href = 0.0001
for n in range(int(1.e-8+T/href)):
    exact = rk4(exact,href)

print('Reference solution is ',exact)
print('\n')

print('For h=0.002 (all methods are stable), h=0.001 and h=0.0005 we solve the problem and compute the error (with the reference solution)')
print('To measure the convergence rate we compute |xref - x_{h/2}| / |xref - x_h|')
print('Error reduction of 2 is linear convergence, 4 is quadratic, 16 is order 4')


errors = np.zeros((5,3))


for hi in range(4):     # three successive refinements of the mehs size
    h = 0.002*0.5**hi   # h=0.002, h=0.001, h=0.0005
    
    N = int(1.e-8+T/h)  # set number of steps
    
    
    x = np.array([1,1,0])  # set initial value
    for i in range(N):
        x = eeuler(x,h)
    errors[hi,0] = np.linalg.norm(x-exact)
    
    x = np.array([1,1,0])  # set initial value
    for i in range(N):
        x = heun(x,h)
    errors[hi,1] = np.linalg.norm(x-exact)

    x = np.array([1,1,0])  # set initial value
    for i in range(N):
        x = rk4(x,h)
    errors[hi,2] = np.linalg.norm(x-exact)

## compute reduction factor
# error(h) / error(h/2)
reduction = errors.copy()
reduction[3,:] = errors[2,:]/errors[3,:]  
reduction[2,:] = errors[1,:]/errors[2,:]  
reduction[1,:] = errors[0,:]/errors[1,:]
reduction[0,:] = np.zeros(3)

print('Errors and error reduction:\n')
print('h\t\tEuler\t\t\t\tHeun\t\t\t\t\tRK4')

for hi in range(4):
    print('{0:2.4f}'.format(0.002*0.5**hi),end='\t')
    
    print('{0:2.4e} ({1:2.2f})\t{2:2.4e} ({3:2.2f})\t{4:2.4e} ({5:2.2f})\t'.format
          (errors[hi,0],reduction[hi,0],errors[hi,1],reduction[hi,1],errors[hi,2],reduction[hi,2]))

print('Euler is first order')
print('Heun is second order (if h is small enough)')
print('Runge-Kutta is very accurate. The error is already as small as the machine precision. From 0.002 to 0.001 the reduction is about 16 which is Order 4')


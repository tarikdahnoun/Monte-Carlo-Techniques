#Day 17 Homework 1
#Monte Carlo Method
#Freshnal Integral

import numpy as np
import pylab as py
import random

xi=0.
xf=2.
nts=5000 #Number of runs
X=np.linspace(xi,xf,nts)

def function(x):
    return np.cos(np.pi*x**2/2)
    
def midpoint(): 
    x=np.linspace(xi,xf,nts)
    dx=x[1]-x[0]
    
    y=np.zeros(nts)
    for i in range(0,nts-1):
        y[i]=function(x[i]+dx/2)*dx
    I=sum(y)
    return y,I
Iv,In=midpoint()
print "The integral using midpoint method is",In
    
I=np.zeros(nts)
def MC_func(nts):
    for i in range(nts):
        r=random.randint(0,nts-1)
        I[i]=Iv[r]
    II=sum(I)
    return II
II=MC_func(nts)
print "The integral using MC method is",II

data=np.zeros(nts)
for i in range(nts):
    data[i]=MC_func(nts)
    
a=np.mean(data)

#The exact value comes from the exercise
std_err=abs(0.488253406075-II)
print "Standard Error is",std_err
std_dev=np.std(data)
print "Standard Deviation is",std_dev 

G=(1/(np.sqrt(2*np.pi*(std_dev**2))))*np.exp((-((X-a)**2))/(2*(std_dev**2)))
py.plot(X,G)
py.xlim(0,1)
py.ylim(0,15)

py.hist(data,bins=50,normed=True)
py.show()

# print G

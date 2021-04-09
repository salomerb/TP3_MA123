import math
from math import *

#Question 1

def Newton (f,fder,x0,epsilon,Nitermax): 
    xold = x0
    if fder(xold) == 0: return xold, 0
    xnew = xold - f(xold)/fder(xold)
    n = 1 
    while abs(xnew-xold)>epsilon and n < Nitermax:
        xold = xnew
        if fder(xold) == 0: break
        xnew = xold - f(xold)/fder(xold)
        n = n+1
    return xnew, n 
 #Question 2

#Définir les fonctions à étudier 
#Définir leurs dérivées 

def f1(x):
    return x**4 + 3*x-9
def f1der (x):
    return 4*(x**3) + 3

def f2(x):
    return x-3*cos(x)+2
def f2der(x):
    return 1 + 3*sin(x)

def f3(x):
    return x*math.exp(x)-7
def f3der(x):
    return math.exp(x) + x*math.exp(x)

def f4(x):
    return math.exp(x)-x-10 
def f4der(x):
    return math.exp(x)-1

def f5(x):
    return 2*math.tan(x)-x-5

def f5der(x):
    return ( 2 / math.cos(x) ** 2 ) - 1

def f6(x):
    return math.exp(x)-(x**2)-3
def f6der(x):
    return math.exp(x)-2*x

def f7(x):
    return 3*x + 4*log(x) - 7
def f7der(x):
    return 3 + (4/x)

def f8(x):
    return x**4 + 2*(x**2) + 4*x - 17
def f8der(x):
    return 4*(x**3) + 4*x + 4 

def f9(x):
    return math.exp(x)-2*math.sin(x) -7 
def f9der(x):
    return math.exp(x)-2*math.cos(x)

def f10(x):
    return ((log(x**2 + 4))*math.exp(x)) - 10
def f10der(x):
    return (2*x/x**2)*math.exp(x)+(log((x**2)+4))*math.exp(x)

#afficher les fonctions  

print(Newton(f1,f1der,0,1e-10,5e4))
print(Newton(f2,f2der,0,1e-10,5e4))
print(Newton(f3,f3der,0,1e-10,5e4))
print(Newton(f4,f4der,0,1e-10,5e4)) 
# print(Newton(f5,f5der,0,1e-10,5e4)) converge pas
print(Newton(f6,f6der,0,1e-10,5e4))
print(Newton(f7,f7der,1,1e-10,5e4))
print(Newton(f8,f8der,1,1e-10,5e4))
print(Newton(f9,f9der,0,1e-10,5e4))
print(Newton(f10,f10der,1,1e-10,5e4))

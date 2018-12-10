"""Module for performing special functions on ADnum objects.
Take an ADnum object as input and return an ADnum object as output.
"""
import numpy as np
from AD20.ADnum import ADnum 


#TRIGONOMETRIC FUNCTIONS
def sin(X):
    try:
        return ADnum(np.sin(X.val), np.cos(X.val)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return sin(X)

def cos(X):
    try:
        return ADnum(np.cos(X.val), -np.sin(X.val)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return cos(X)

def tan(X):
    try:
        return ADnum(np.tan(X.val), (1/np.cos(X.val)**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return tan(X)

def csc(X):
    try:
        return ADnum(1/np.sin(X.val), (-1/np.tan(X.val))*(1/np.sin(X.val))*X.der)
    except:
        X = ADnum(X, 0)
        return csc(X)

def sec(X):
    try:
        return ADnum(1/np.cos(X.val), np.tan(X.val)/np.cos(X.val)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return sec(X)

def cot(X):
    try:
        return ADnum(1/np.tan(X.val), -1/(np.sin(X.val)**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return cot(X)

#INVERSE TRIGONOMETRIC FUNCTIONS
def arcsin(X):
    try:
        return ADnum(np.arcsin(X.val), 1/np.sqrt(1-X.val**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return arcsin(X)

def arccos(X):
    try:
        return ADnum(np.arccos(X.val), -1/np.sqrt(1-X.val**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return arccos(X)

def arctan(X):
    try:
        return ADnum(np.arctan(X.val), 1/(1+X.val**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return arctan(X)

#HYPERBOLIC TRIG FUNCTIONS
def sinh(X):
    try:
        return ADnum(np.sinh(X.val), np.cosh(X.val)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return sinh(X)

def cosh(X):
    try:
        return ADnum(np.cosh(X.val), np.sinh(X.val)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return cosh(X)

def tanh(X):
    try:
        return ADnum(np.tanh(X.val), 1/(np.cosh(X.val)**2)*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return tanh(X)

#NATURAL EXPONENTIAL AND NATURAL LOGARITHM
def exp(X):
    try:
        return ADnum(np.exp(X.val), np.exp(X.val)*X.der)
    except AttributeError:
        X = ADnum(X,0)
        return exp(X)

def log(X):
    try:
        return ADnum(np.log(X.val), 1/X.val*X.der)
    except AttributeError:
        X = ADnum(X, 0)
        return log(X)





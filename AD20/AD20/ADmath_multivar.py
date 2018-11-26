"""Module for performing special functions on ADnum objects.
Take an ADnum object as input and return an ADnum object as output.
"""
import AD20
import numpy as np
from AD20.ADnum_multivar import ADnum


#TRIGONOMETRIC FUNCTIONS
def sin(X):
    try:
        return ADnum(np.sin(X.val), der = np.cos(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.sin(X)

def cos(X):
    try:
        return ADnum(np.cos(X.val), der = -np.sin(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.cos(X)

def tan(X):
    try:
        return ADnum(np.tan(X.val), der = (1/np.cos(X.val)**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.tan(X)

def csc(X):
    try:
        return ADnum(1/np.sin(X.val), der = (-1/np.tan(X.val))*(1/np.sin(X.val))*X.der)
    except:
        # X = ADnum(X, 0)
        return 1/np.sin(X.val)

def sec(X):
    try:
        return ADnum(1/np.cos(X.val), der = np.tan(X.val)/np.cos(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return 1/np.cos(X.val)

def cot(X):
    try:
        return ADnum(1/np.tan(X.val), der = -1/(np.sin(X.val)**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return 1/np.tan(X.val)

#INVERSE TRIGONOMETRIC FUNCTIONS
def arcsin(X):
    try:
        return ADnum(np.arcsin(X.val), der = 1/np.sqrt(1-X.val**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.arcsin(X)

def arccos(X):
    try:
        return ADnum(np.arccos(X.val), der = -1/np.sqrt(1-X.val**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.arccos(X)

def arctan(X):
    try:
        return ADnum(np.arctan(X.val), der = 1/(1+X.val**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.arctan(X)

#HYPERBOLIC TRIG FUNCTIONS
def sinh(X):
    try:
        return ADnum(np.sinh(X.val), der = np.cosh(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.sinh(X)

def cosh(X):
    try:
        return ADnum(np.cosh(X.val), der = np.sinh(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.cosh(X)

def tanh(X):
    try:
        return ADnum(np.tanh(X.val), der = 1/(np.cosh(X.val)**2)*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.tanh(X)

#NATURAL EXPONENTIAL AND NATURAL LOGARITHM
def exp(X):
    try:
        return ADnum(np.exp(X.val), der = np.exp(X.val)*X.der)
    except AttributeError:
        # X = ADnum(X,0)
        return np.exp(X)

def log(X):
    try:
        return ADnum(np.log(X.val), der = 1/X.val*X.der)
    except AttributeError:
        # X = ADnum(X, 0)
        return np.log(X)





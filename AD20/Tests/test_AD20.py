import pytest
import numpy as np
from AD20.ADnum import ADnum
from AD20 import ADmath

def test_ADmath_sin():
    X = ADnum(np.pi)
    Y = ADmath.sin(X)
    assert Y.val == np.sin(np.pi)
    assert Y.der == np.cos(np.pi)

def test_ADmath_cos():
    f = ADmath.cos(ADnum(4))
    assert f.val == np.cos(4)
    assert f.der == -np.sin(4)

def test_ADmath_tan():
    f = ADmath.tan(ADnum(4))
    assert f.val == np.tan(4)
    assert f.der == (1/np.cos(4))**2


def test_ADnum_mul():
    x = ADnum(3.0)
    f = x*2.0
    assert f.val == 6.0
    assert f.der == 2.0

def test_ADnum_rmul():
    x = ADnum(3.0)
    f = 2.0*x
    assert f.val == 6.0
    assert f.der == 2.0

def test_ADnum_add():
    x = ADnum(3.0)
    f = x+2.0
    assert f.val == 5.0
    assert f.der == 1.0

def test_ADnum_radd():
    x = ADnum(3.0)
    f = 2.0+x
    assert f.val == 5.0
    assert f.der == 1.0

def test_ADnum_sub():
    x = ADnum(5.0)
    f = x-2.0
    assert f.val == 3.0
    assert f.der == 1.0

def test_ADnum_rsub():
    x = ADnum(3.0)
    f = 5.0-x
    assert f.val == 2.0
    assert f.der == -1.0

def test_ADnum_div():
    x = ADnum(3.0)
    f = x/1.5
    assert f.val == 2.0
    assert f.der == 1/1.5

def test_ADnum_rdiv():
    x = ADnum(3.0)
    f = 6/x
    assert f.val == 2.0
    assert f.der == -2/3

def test_ADnum_pow():
    x = ADnum(3.0)
    f = x**2.0
    assert f.val == 9.0
    assert f.der == 6.0

def test_ADnum_rpow():
    x = ADnum(3.0)
    f = 4**x
    assert f.val == 64
    assert f.der == 64*np.log(4.0)

def test_12x():
    x = ADnum(1)
    f = 1/(1-2*x)
    assert f.val == 1/(1-2)
    assert f.der == 2/(1-2)**2

def test_xex():
    x = ADnum(2)
    f = x * ADmath.exp(x)
    assert f.val == 2.0 * np.exp(2.0)
    assert f.der == np.exp(2.0) + 2.0*np.exp(2.0)

def test_5x2lnx():
    x = ADnum(1)
    f = 5 * x**2 * ADmath.log(x)
    assert f.val == 0.0
    assert f.der == 10 * x * np.log(1.0) + 5*1.0

def test_sinxcosx():
    x = ADnum(0)
    f = ADmath.sin(x) * ADmath.cos(x)
    assert f.val == np.sin(0) * np.cos(0)
    assert f.der == -(np.sin(0) ** 2) + np.cos(0) **2

def test_2xe2x():
    x = ADnum(2)
    f = 2 * x * ADmath.exp(2*x)
    assert f.val == 4 * np.exp(4)
    assert f.der == 2 * np.exp(4.0) + 8 * np.exp(4)



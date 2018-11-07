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
    x = ADnum(3.0)
    f = x-2.0
    assert f.val == 1.0
    assert f.der == 1.0

def test_ADnum_rsub():
    x = ADnum(3.0)
    f = 5.0-x
    assert f.val == 2.0
    assert f.der == 1.0

def test_ADnum_div():
    x = ADnum(3.0)
    f = x/1.5
    assert f.val == 2
    assert f.der == 1.5

def test_ADnum_rsub():
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
    f = np.e**x
    assert f.val == np.exp(3.0)
    assert f.der == np.exp(3.0)
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



import pytest
import ADnum
import ADmath

def test_ADmath_sin():
    X = ADnum(np.pi)
    Y = ADmath.sin(X)
    assert Y.val == 0
    assert Y.der == -1

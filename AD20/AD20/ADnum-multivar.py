"""Module to wrap numbers into ADnum object and do basic calculations.
Take value and specified derivative as given, wrap up as ADnum object, and return ADnum object for each basic calculation function.
"""
import numpy as np
class ADnum:
    """ Class to create ADnum objects on which to perform differentiation.

    ATTRIBUTES
    ==========
    val : scalar for scalar valued quantities or numpy array for vector valued functions, the value of the ADnum object for a set input value
    der: scalar for sclar functions of a single variable or numpy array for functions of multiple variables the derivative 
    
    METHODS
    =======
    This class overloads the methods for basic arithmetic operations.

    EXAMPLES
    ========
    #>>> x = ADnum(2)
    #>>> f = 2*x+3
    #>>> print(f.val)
    #7.0
    #>>> print(f.der)
    #2.0
    """
    def __init__(self, value, **kwargs):
        try:
            value = value.astype(float)
            if 'der' not in kwargs:
                try:
                    ins = kwargs['ins']
                    ind = kwargs['ind']
                    der = np.zeros(ins) #need to change to matrix if len(val) is not 1
                    der[ind] = 1.0
                except:
                    raise KeyError('Must provide ins and ind if der not provided.')
            else:
                der = kwargs['der']
                der = der.astype(float)
                if 'ins' in kwargs:
                    ins = kwargs['ins']
                    if len(der) != ins:
                        raise ValueError('Shape of derivative does not match number of inputs.')
        except:
            raise ValueError('Value and derivative of ADnum object must be numeric.')
        self.val = value
        self.der = der

    def __mul__(self,other):
        try:
            return ADnum(self.val*other.val, self.val*other.der+self.der*other.val)
        except AttributeError:
            other = ADnum(other*np.ones(np.shape(self.val)), der = np.zeros(np.shape(self.der)))
            return self*other

    def __rmul__(self,other):
        return self.__mul__(other)

    def __add__(self,other):
        try:
            return ADnum(self.val+other.val, self.der+other.der)
        except AttributeError:
            other = ADnum(other, 0)
            return self + other

    def __radd__(self,other):
        return self.__add__(other)

    def __sub__(self,other):
        try:
            return ADnum(self.val-other.val,self.der-other.der)
        except AttributeError:
            other = ADnum(other, 0)
            return self-other

    def __rsub__(self, other):
        try:
            return ADnum(other.val-self.val, other.der-self.der)
        except AttributeError:
            other = ADnum(other, 0)
            return other-self

    def __truediv__(self, other):
        try:
            return ADnum(self.val/other.val, (other.val*self.der-self.val*other.der)/(other.val**2))
        except AttributeError:
            other = ADnum(other, 0)
            return self/other
    
    def __rtruediv__(self, other):
        try:
            return ADnum(other.val/self.val, (self.val*other.der-other.val*self.der)/(self.val**2))
        except AttributeError:
            other = ADnum(other, 0)
            return other/self

    def __pow__(self, other, modulo=None):
        try:
            return ADnum(self.val**other.val, other.val*(self.val**(other.val-1))*self.der+(self.val**other.val)*np.log(np.abs(self.val))*other.der)

        except AttributeError:
            other = ADnum(other, 0)
            return self**other

    def __rpow__(self, other):
        try:
            return ADnum(other.val**self.val, self.val*(other.val**(self.val-1))*other.der+(other.val**self.val)*np.log(other.val)*self.der)
        except AttributeError:
            other = ADnum(other, 0)
            return other**self

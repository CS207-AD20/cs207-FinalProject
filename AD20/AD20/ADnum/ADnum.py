import numpy as np
class ADnum:
    def __init__(self, value, der = 1): #this needs to be modified for multivar--For der default value, we only allow it to be default for single numbers, otherwise, the user should declare it.
        self.val = value
        self.der = der

    def __mul__(self,other):
        try:
            return ADnum(self.var*other.val, self.val*other.der+self.der*other.val)
        except AttributeError:
            return ADnum(self.val*other, other*self.der)

    def __rmul__(self,other):
        try:
            return ADnum(self.val*other.val, self.val*other.der+self.der*other.val)
        except AttributeError:
            return ADnum(self.val*other, other*self.der)

    def __add__(self,other):
        try:
            return ADnum(self.val+other.val, self.der+other.der)
        except AttributeError:
            return ADnum(self.val+other, self.der)

    def __radd__(self,other):
        try:
            return ADnum(self.val+other.val,self.der+other.der)
        except AttributeError:
            return ADnum(self.val+other, self.der)

    def __sub__(self,other):
        try:
            return ADnum(self.val-other.val,self.der-other.der)
        except AttributeError:
            return ADnum(self.val-other,self.der)
    def __rsub__(self, other):
        try:
            return ADnum(other.val-self.val, other.der-self.der)
        except AttributeError:
            return ADnum(other-self.val, self.der)

    def __div__(self, other):
        try:
            return ADnum(self.val/other.val, (other.val*self.der-self.val*other.der)/(other.val**2))
        except AttributeError:
            return ADnum(self.val/other,(1/other.val)*self.der)
    def __rdiv__(self, other):
        try:
            return ADnum(other.val/self.val, (self.val*other.der-other.val*self.der)/(self.val**2))
        except AttributeError:
            return ADnum(other/self.val, other.val(self.))

    def __pow__(self, other, modulo=None):
        ###???Questions on this method:
        # 1. there won't be the case for x**f(x)???
        # 2. Do we  need to differentiate constant term with the term that is constant to x?
        # try:### the common case is that power is a constant term wrt x
        #     return ADnum(self.val**power.val, power.val*(self.val**(power.val-1)))
        # except AttributeError:
        #
        #     return ADnum(1/self.val, )
        try:
            return ADnum(self.val**other.val, other.val*(self.val**(other.val-1))*self.der+(self.der**other.val)*np.log(self.val)*other.der)

        except AttributeError:# when other is constant
            return ADnum(self.val**other, other*(self.val**(other-1))*self.der)

    def __rpow__(self, other):
        try:
            return ADnum(other.val**self.val, self.val*(other.val**(self.val-1))*other.der+(other.der**self.val)*np.log(other.val)*self.der)
        except AttributeError:
            return ADnum(other**self.val, np.log(other)*self.der)
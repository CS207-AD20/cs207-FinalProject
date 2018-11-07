import numpy as np
class ADnum:
    def __init__(self, value, der = 1): #this needs to be modified for multivar--For der default value, we only allow it to be default for single numbers, otherwise, the user should declare it.
        try:
            value = float(value)
            der = float(der)
        except:
            raise TypeError('Value and derivative of ADnum object must be numeric.')
        #if type(value)!= int and type(value)!=float:
         #   raise TypeError('ADnum can only take numeric values.')
        #if type(der)!= int and type(der) !=float:
         #   raise TypeError('Derivative of ADnum must be numberic.')
        self.val = value
        self.der = der

    def __mul__(self,other):
        try:
            return ADnum(self.val*other.val, self.val*other.der+self.der*other.val)
        except AttributeError:
            other = ADnum(other, 0)
            return self*other
            #return ADnum(self.val*other, other*self.der)

    def __rmul__(self,other):
        return self.__mul__(other)
        #try:
            #return ADnum(self.val*other.val, self.val*other.der+self.der*other.val)
        #except AttributeError:
            #return ADnum(self.val*other, other*self.der)

    def __add__(self,other):
        try:
            return ADnum(self.val+other.val, self.der+other.der)
        except AttributeError:
            other = ADnum(other, 0)
            return self + other
            #return ADnum(self.val+other, self.der)

    def __radd__(self,other):
        return self.__add__(other)
        #try:
         #   return ADnum(self.val+other.val,self.der+other.der)
        #except AttributeError:
         #   return ADnum(self.val+other, self.der)

    def __sub__(self,other):
        try:
            return ADnum(self.val-other.val,self.der-other.der)
        except AttributeError:
            return ADnum(self.val-other,self.der)
    def __rsub__(self, other):
        try:
            return ADnum(other.val-self.val, other.der-self.der)
        except AttributeError:
            return ADnum(other-self.val, -self.der)

    def __truediv__(self, other):
        try:
            return ADnum(self.val/other.val, (other.val*self.der-self.val*other.der)/(other.val**2))
        except AttributeError:
            return ADnum(self.val/other,(1/other)*self.der)
    def __rtruediv__(self, other):
        try:
            return ADnum(other.val/self.val, (self.val*other.der-other.val*self.der)/(self.val**2))
        except AttributeError:
            return ADnum(other/self.val, other*self.__pow__(-1).der)

    def __pow__(self, other, modulo=None):
        try:
            return ADnum(self.val**other.val, other.val*(self.val**(other.val-1))*self.der+(self.val**other.val)*np.log(self.val)*other.der)

        except AttributeError:# when other is constant
            return ADnum(self.val**other, other*(self.val**(other-1))*self.der)

    def __rpow__(self, other):
        try:
            return ADnum(other.val**self.val, self.val*(other.val**(self.val-1))*other.der+(other.val**self.val)*np.log(other.val)*self.der)
        except AttributeError:
            return ADnum(other**self.val, (other**self.val)*np.log(other)*self.der)

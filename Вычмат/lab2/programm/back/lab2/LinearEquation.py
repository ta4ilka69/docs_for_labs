from math import exp, sin, cos,sqrt
from typing import List, Callable
class Equations:
    def __init__(self):
        self.eq = [self.first, self.second, self.third, self.fourth]
        self.d = [self.f1, self.f2, self.f3, self.f4]
    @staticmethod
    def first(x):
        return x**2-3*x+1

    @staticmethod
    def second(x):
        return exp(x)-sin(x)+x

    @staticmethod
    def third(x):
        return 1/sin(x)+x**2

    @staticmethod
    def fourth(x):
        return exp(x)-x**2+10*cos(x)
    
    @staticmethod
    def f1(x):
        return (2*x+1)/3
    @staticmethod
    def f2(x):
        return cos(x)-exp(x)
    @staticmethod
    def f3(x):
        return -2/(sqrt(1-1/(x**4))*x**3)
    @staticmethod
    def f4(x):
        return (exp(x)-10*sin(x))/2/sqrt(abs(exp(x)+10*cos(x)))

    def binary_search(self, a, b, eps, i):
        k = 0
        x = (a+b)/2
        while abs(a-b) > eps:
            x = (a+b)/2
            if self.eq[i](a)*self.eq[i](x) < 0:
                b = x
            else:
                a = x
            k+=1
        return {"x": x, "f": self.eq[i](x), "k":k}
    
    def check_for_roots(self,a,b,i,s):
        if(self.eq[i](a)*self.eq[i](b)>0):
            raise ValueError("The function has no roots in the given interval")
    
    def secant_method(self, a, b, eps, i):
        k = 0
        x = [a]
        x.append((a+b)/2)
        while abs(self.eq[i](x[-1]))>eps:
            x.append(x[-1]-(x[-1]-x[-2])/(self.eq[i](x[-1])-self.eq[i](x[-2]))*self.eq[i](x[-1]))
            k+=1
        return {"x": x[-1], "f": self.eq[i](x[-1]), "k":k}
    
    def simple_iteration(self,a,b,eps,i):
        k = 0
        s = True
        m = 0
        for x in range(int(a/eps),int(b/eps),int(eps/eps)):
            if abs(self.d[i](x))>1:
                s = False
                if abs(self.d[i](x))>m:
                    m = abs(self.d[i](x))
        x = (a+b)/2
        if s:
            x = x - 1/m*self.d[i](x)
            while abs(self.eq[i](x))>eps:
                x = x - 1/m*self.d[i](x)
                k+=1
            if (x == x - 1/m*self.d[i](x)):
                raise IndexError("The method is not converging")
            return {"x": x, "f": self.eq[i](x), "k":k}
        else:
            k = 0
            x = (a+b)/2
            x = x - 1/m*self.d[i](x)
            while abs(self.eq[i](x))>eps:
                x = x - 1/m*self.d[i](x)
                k+=1
                if k>200:
                    raise IndexError("The method is not converging")
            if (x == x - 1/m*self.d[i](x)):
                raise IndexError("The method is not converging")
            return {"x": x, "f": self.eq[i](x), "k":k}

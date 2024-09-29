from util import Printing
import numpy as np
class gradMethods:
    def __init__(self, x0,y0,e,f,fx,fy):
        self.x0 = x0
        self.y0 = y0
        self.e = e
        self.f = f
        self.fx = fx
        self.fy = fy
        self.lambd = 0.25
    def absgrad(self,x,y):
        return np.sqrt(self.fx(x)**2 + self.fy(y)**2)
    def gradDescent(self):
        strparam = ["xk", "yk", "f'_x(xk)", "f'_y(yk)", "xk+1","yk+1","f(x(k+1))"," |gradf|"]
        res = []
        x = self.x0
        y = self.y0
        k = 0
        while True:
            k += 1
            temp = []
            temp.append(x)
            temp.append(y)
            temp.append(self.fx(x))
            temp.append(self.fy(y))
            x = x - self.lambd*self.fx(x)
            y = y - self.lambd*self.fy(y)
            temp.append(x)
            temp.append(y)
            temp.append(self.f(x,y))
            temp.append(self.absgrad(x,y))
            res.append(temp)
            if temp[-1] < self.e:
                break
            if k>100:
                raise OverflowError("Too many iterations. Try another starting point")
        return Printing(strparam,res)
    
    def h1_calc(self,a,b):
        return ((2*a-4)**2+(6-2*b)**2)/(2*(2*a-4)**2-2*(6-2*b)**2)
    
    #метод наискорейшего спуска
    def fastestDescent(self):
        strparam = ["xk", "yk", "f'_x(xk)", "f'_y(yk)", "xk+1","yk+1","f(x(k+1))","h1"," |gradf|"]
        res = []
        x = self.x0
        y = self.y0
        k = 0
        while True:
            k += 1
            temp = []
            temp.append(x)
            temp.append(y)
            temp.append(self.fx(x))
            temp.append(self.fy(y))
            try:
                h1 = self.h1_calc(x,y)
            except ZeroDivisionError:
                temp.append(x)
                temp.append(y)
                temp.append(self.f(x,y))
                temp.append(0)
                temp.append(self.absgrad(temp[-3],temp[-2]))
                res.append(temp)
                break
            x = x - h1*self.fx(x)
            y = y - h1*self.fy(y)
            temp.append(x)
            temp.append(y)
            temp.append(self.f(x,y))
            temp.append(h1)
            temp.append(self.absgrad(temp[-3],temp[-2]))
            res.append(temp)
            if temp[-1] < self.e:
                break
            if k>100:
                raise OverflowError("Too many iterations. Try another starting point")
        return Printing(strparam,res)

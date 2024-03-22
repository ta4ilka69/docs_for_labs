
class square_approximation:
    def __init__(self,a,b,e,f,dx):
        self.a = a
        self.b = b
        self.e = e
        self.f = f
        self.dx = dx
        self.x1 = None
        self.x2 = None
        self.x3 = None
        self.f1 = None
        self.f2 = None
        self.f3 = None
        self.result = []
#____________________________________________________________________________________
    def main(self,x_start):
        self.x1 = x_start
        self.x2 = x_start + self.dx
        self.f1 = self.f(self.x1)
        self.f2 = self.f(self.x2)
        if self.f1 > self.f2:
            self.x3 = self.x1 + 2 * self.dx
        else:
            self.x3 = self.x1 - self.dx
        self.f3 = self.f(self.x3)
        return self.finding_minimum()

    def finding_minimum(self):
        Fmin = min(self.f1, self.f2, self.f3)
        if Fmin == self.f1:
            x_min = self.x1
        elif Fmin == self.f2:
            x_min = self.x2
        else:
            x_min = self.x3
        denominator = 2*((self.x2-self.x3)*self.f1 + (self.x3-self.x1)*self.f2+(self.x1-self.x2)*self.f3)
        numerator = (self.x2**2-self.x3**2)*self.f1 + (self.x3**2-self.x1**2)*self.f2 + (self.x1**2-self.x2**2)*self.f3
        self.result.append([self.x1, self.x2, self.x3, self.f1, self.f2, self.f3, x_min, Fmin, numerator,denominator,False,False,False,False])
        if denominator == 0:
            return self.main(x_min)
        x_current = numerator/denominator
        self.check(x_current,x_min)
    
    def check(self, x_current, x_min):
        f_current = self.f(x_current)
        self.result[-1][-4] = x_current
        self.result[-1][-3] = f_current
        f_min = self.f(x_min)
        first_condition = abs((f_min-f_current)/(f_current)) < self.e
        second_condition = abs((x_min-x_current)/(x_current)) < self.e
        third_condition = x_current>=self.x1 and x_current<=self.x3
        self.result[-1][-2] = bool(first_condition)
        self.result[-1][-1] = bool(second_condition)
        if first_condition and second_condition:
            return x_current
        elif third_condition:
            xs = [self.x1,self.x2,self.x3,x_current]
            xs.sort()
            self.x2 = x_current
            self.x1 = xs[xs.index(x_current)-1]
            self.x3 = xs[xs.index(x_current)+1]
            self.f1 = self.f(self.x1)
            self.f2 = self.f(self.x2)
            self.f3 = self.f(self.x3)
            return self.finding_minimum()
        else:
            return self.main(x_current)
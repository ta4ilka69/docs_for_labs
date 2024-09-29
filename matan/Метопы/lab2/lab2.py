from util import Printing

class function:
    def __init__(self, a,b,e,f,f_x,f_xx):
        self.a = a
        self.b = b
        self.e = e
        self.f = f
        self.f_x = f_x
        self.f_xx = f_xx

    def bisecting(self):
        a = self.a
        b = self.b
        e = self.e
        res = []
        while abs(b - a) > 2*e:
            row = [a,b]
            x1 = (a+b-e)/2
            x2 = (a+b+e)/2
            row.append(x1)
            row.append(x2)
            fx1 = self.f(x1)
            fx2 = self.f(x2)
            row.append(fx1)
            row.append(fx2)
            xm = (a+b)/2
            fxm = self.f(xm)
            row.append(xm)
            row.append(fxm)
            if fx1>fx2:
                a = x1
            else:
                b = x2
            res.append(row)
        return Printing(["a", "b", "x1", "x2","f(x1)","f(x2)","x","f(x)"], res)

    def gold_section(self):
        a = self.a
        b = self.b
        e = self.e
        res = []
        while abs(b - a) > 2*e:
            row = [a,b]
            if len(res)==0:
                x1 = a + 0.382*(b-a)
                x2 = a + 0.618*(b-a)
            row.append(x1)
            row.append(x2)
            fx1 = self.f(x1)
            fx2 = self.f(x2)
            row.append(fx1)
            row.append(fx2)
            x = (a+b)/2
            row.append(x)
            row.append(self.f(x))
            if fx1>fx2:
                a = x1
                x1 = x2
                x2 = a + 0.618*(b-a)
            else:
                b = x2
                x2 = x1
                x1 = a + 0.382*(b-a)
            res.append(row)
        return Printing(["a", "b", "x1", "x2","f(x1)","f(x2)","x","f(x)"], res)
    
    def chord(self):
        a = self.a
        b = self.b
        e = self.e
        res = []
        f_x_x = 10**10
        while abs(f_x_x) > e:
            row = [a,b]
            f_x_a = self.f_x(a)
            f_x_b = self.f_x(b)
            row.append(f_x_a)
            row.append(f_x_b)
            x = a - f_x_a*(a-b)/(f_x_a-f_x_b)
            row.append(x)
            f_x_x = self.f_x(x)
            row.append(f_x_x)
            row.append(self.f(x))
            if self.f_x(x) > 0:
                b = x
            else:
                a = x
            res.append(row)
        return Printing(["a", "b", "f'(a)","f'(b)","x","f'(x)","f(x)"], res)
    
    def newton(self):
        a = self.a
        b = self.b
        e = self.e
        res = []
        x = (a+b)/2
        f_x_x = self.f_x(x)
        while abs(f_x_x) >= e:
            row = [x]
            f_x_x = self.f_x(x)
            f_xx_x = self.f_xx(x)
            row.append(f_x_x)
            row.append(f_xx_x)
            x = x - f_x_x/f_xx_x
            row.append(self.f(x))
            res.append(row)
        return Printing(["x", "f'(x)","f''(x)","f(x)"], res)
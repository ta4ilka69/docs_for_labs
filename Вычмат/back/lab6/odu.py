from numpy import exp, inf, divide
class Odu:
    @staticmethod
    def get_constant_1(x0,y0):
        return -exp(x0)*x0-divide(exp(x0),y0)
    @staticmethod
    def y1(x,y,c):
        return divide(-exp(x),c+exp(x)*x)
    @staticmethod
    def get_constant_2(x0,y0):
        return divide(y0-x0-1,exp(x0))
    @staticmethod
    def y2(x,y,c):
        return c*exp(x)+x+1
    @staticmethod
    def get_constant_3(x0,y0):
        return divide(y0-divide(exp(x0),2),exp(-x0))
    @staticmethod
    def y3(x,y,c):
        return c*exp(-x)+divide(exp(x),2)
    @staticmethod
    def f1(x,y):
        return y+(1+x)*y**2
    @staticmethod
    def f2(x,y):
        return y-x
    @staticmethod
    def f3(x,y):
        return -y+exp(x)
    def __init__(self,x,y,b,f,e):
        assert x!=b, "The interval is empty"
        if(f==1):
            self.f = self.f1
            self.constant = self.get_constant_1(x,y)
            self.y = self.y1
        elif(f==2):
            self.f = self.f2
            self.constant = self.get_constant_2(x,y)
            self.y = self.y2
        elif(f==3):
            self.f = self.f3
            self.constant = self.get_constant_3(x,y)
            self.y = self.y3
        assert self.constant is not inf, "The constant is infinite"
        self.y0 = y
        self.a = x
        self.b = b
        self.e = e
    def Eiler(self):
        h = self.b-self.a
        res = self.Eiler_mod(h)
        while not res[0]:
            h = h/2
            x = res[1].copy()
            check = res[2].copy()
            res = self.Eiler_mod(h,check[-1])
        return [x,check]
        
        
    #Контролируем точность конечного интервала
    
    def Eiler_mod(self,h,check=None):
        x = [self.a]
        while x[-1]<self.b:
            x.append(x[-1]+h)
        y = [self.y0]
        for x_ in x[:len(x)-1]:
            y.append(y[-1]+h*self.f(x_,y[-1]))
        if check!=None:
            if abs(y[-1]-check)<self.e:
                return [True,[],[]]
            else:
                return [False,x,y]
        else:
            return [False,x,y]
    
    def Runge_Kutta(self):
        h = self.b-self.a
        res = self.Runge_Kutta_mod(h)
        while not res[0]:
            h = h/2
            x = res[1].copy()
            check = res[2].copy()
            res = self.Runge_Kutta_mod(h,check[-1])
        return [x,check]
    
    def Runge_Kutta_mod(self,h,check=None):
        x = [self.a]
        while x[-1]<self.b:
            x.append(x[-1]+h)
        y = [self.y0]
        for x_ in x[:len(x)-1]:
            k1 = h*self.f(x_,y[-1])
            k2 = h*self.f(x_+h/2,y[-1]+k1/2)
            k3 = h*self.f(x_+h/2,y[-1]+k2/2)
            k4 = h*self.f(x_+h,y[-1]+k3)
            y.append(y[-1]+(k1+2*k2+2*k3+k4)/6)
        if check!=None:
            if abs(y[-1]-check)<self.e:
                return [True,[],[]]
            else:
                return [False,x,y]
        else:
            return [False,x,y]
    
    
    def Milne(self,h=None):
        if h is None:
            h = (self.b-self.a)/4
        x = [self.a]
        while x[-1]<self.b:
            x.append(x[-1]+h)
        y = [self.y0]
        for x_ in x[:3]:
            y.append(y[-1]+h*self.f(x_,y[-1]))
        f = [self.f(x[i],y[i]) for i in range(3)]
        y_progn = y[-4]+4*h/3*(2*f[-1]-f[-2]+2*f[-3])
        f_prog = 0
        y_corr = 0
        i = 4
        while len(y)!=len(x):
            f_prog = self.f(x[i],y_progn)
            y_corr = y[-2]+h/3*(f[-2]+4*f[-1]+f_prog)
            if(abs(y_corr-y_progn)<self.e):
                y.append(y_corr)
                f.append(f_prog)
                y_progn = y[-4]+4*h/3*(2*f[-1]-f[-2]+2*f[-3])
            else:
                y_progn = y_corr
                i-=1
            i+=1
        T = True
        for i in range(len(y)):
            if abs(y[i]-self.y(x[i],y[i],self.constant))>self.e:
                T = False
                break
        if T:
            return [x,y]
        else:
            return self.Milne(h/2)
                
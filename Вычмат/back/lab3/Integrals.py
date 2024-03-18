from numpy import sin,pi, sqrt, exp, cos, nan,divide
from lab3.Answer import Answer
class Integrals:
#_________________________________________________________________________________
    f1 = lambda x: (x-1)**2
    f2 = lambda x: sin(pi*x)/2
    f3 = lambda x: (sqrt(x))/(exp(x)-1)
    f4 = lambda x: cos(pi*x)-exp(sin(pi*x))+1
    f5 = lambda x: divide(divide(1,(x-1)),(x-2))
    functions = [f1, f2, f3, f4, f5]
#_________________________________________________________________________________
    def check_converging(self,risks):
        miss = 0
        for i in range(len(risks)-1):
            if abs(risks[i])<abs(risks[i+1]):
                miss+=1
            else:
                miss=0
            if miss>3:
                raise ValueError("The integral is not converging")
        
            
#_________________________________________________________________________________
    def integrating(self,mode,depth=0):
        previous_int = 10**10
        darbu_sums = 0
        current_partions = self.partions
        risks = []
        while abs(previous_int-darbu_sums) > self.eps/2 or current_partions==self.partions*2:
            previous_int = darbu_sums
            darbu_sums = 0
            h = (self.b - self.a)/current_partions
            for i in range(current_partions):
                 darbu_sums += mode(h,i)
            darbu_sums *= h
            current_partions *= 2
                         #checking converging
            if(current_partions>self.partions*2):
                risks.append(darbu_sums-previous_int)
            if len(risks)%10 == 0 and len(risks)!=0:
                self.check_converging(risks)
                risks.clear()
            if current_partions>2**21:
                darbu_sums = nan
                break
        if (str(darbu_sums) == str(nan)) and depth==0:
            self.partions *= 2
            return self.integrating(mode,1)
        elif (str(darbu_sums) == str(nan)) and depth==1:
            self.a = self.a+self.eps**2
            return self.integrating(mode,2)
        elif (str(darbu_sums) == str(nan)) and depth==2:
            self.b = self.b-self.eps**2
            return self.integrating(mode,3)
        elif (str(darbu_sums) == str(nan)) and depth==3 and current_partions<=2**21 or "inf" in str(darbu_sums) or "inf" in str(previous_int):
            raise ValueError("The integral is not converging or the function is not defined in the given interval")
        elif current_partions>2**21 and depth==3:
            raise ValueError("Computation time exceeded, try to use another method or decrease the interval length") 
        else:
            return Answer(darbu_sums,current_partions//2)
#_________________________________________________________________________________
    def rectangle(self,mode):
        return self.integrating(lambda h,step: self.current_function(self.a + h*mode(step)))
    def rectangle_rights(self):
        return self.rectangle(lambda step: step+1)
    def rectangle_lefts(self):
        return self.rectangle(lambda step: step)
    def rectangle_middles(self):
        return self.rectangle(lambda step: step+0.5)
#_________________________________________________________________________________
    def trapezoid(self):
        return self.integrating(lambda h,step: (self.current_function(self.a + h*step)+self.current_function(self.a + h*(step+1)))/2)   
#_________________________________________________________________________________
    def simpson(self):
        return self.integrating(lambda h,step: (self.current_function(self.a + h*step) +
                                             4*self.current_function(self.a + h*(step+0.5)) +
                                             self.current_function(self.a + h*(step+1))) / 6)
#_________________________________________________________________________________
    methods = [rectangle_lefts, rectangle_rights, rectangle_middles, trapezoid, simpson]
#_________________________________________________________________________________
    def __init__(self, a, b, equathion, method, eps):
        self.a = a
        self.b = b
        self.current_function = self.functions[equathion-1]
        self.eps = eps
        self.partions = 4 #const starting number of partions
        self.method = self.methods[method-1]

    def solve(self):
        return self.method(self)
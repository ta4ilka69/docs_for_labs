from math import tan,sin,cos,exp,log
class System:
    @staticmethod
    def firstdx(x,y):
        return (-(x+tan(y)-1)/(sin(x))**2-1/(tan(x))-2*y-3)/(1/(cos(y)**2*sin(x)**2)+2)
    
    @staticmethod
    def firstdy(x,y):
        return -x-tan(y)+1-System.firstdx(x,y)/cos(y)**2
    
    @staticmethod
    def seconddx(x,y):
        return (x+3-log(y)+1+exp(x)/y-5/y)/(-1-exp(x)/y)
    def seconddy(x,y):
        return -exp(x)*System.seconddx(x,y)-y-exp(x)+5
    
    @staticmethod
    def Newton(a0,b0,a,b,e,eq):
        x = a0
        y = b0
        k = 0
        if(eq=="1"):
            while True:
                k+=1
                x1 = x + System.firstdx(x,y)
                y1 = y + System.firstdy(x,y)
                if abs(x1-x)<e and abs(y1-y)<e:
                    return {"x":x1,"y":y1,"k":k}
                x = x1
                y = y1
                if k>=1000:
                    raise ValueError("The function has no roots in the given interval")
        elif(eq=="2"):
            while True:
                k+=1
                x1 = x + System.seconddx(x,y)
                y1 = y + System.seconddy(x,y)
                if abs(x1-x)<e and abs(y1-y)<e:
                    return {"x":x1,"y":y1,"k":k}
                x = x1
                y = y1
                if k>=1000:
                    raise ValueError("The function has no roots in the given interval")
import math
class Interpolation:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.n = len(x)
        assert len(set(x)) == self.n and self.n==len(y), "x values must be unique"
        self.endless = None

    def L(self):
        # return string with the Lagrange polynomial
        L = []
        for i in range(self.n):
            l = [f"({self.y[i]})"]
            for j in range(self.n):
                if i != j:
                    l.append(f"(x-{self.x[j]})/({self.x[i]-self.x[j]})")
            L.append("*".join(l))
        return "+".join(L)
    
    def g(self,i):
        n = len(i)
        if n==1:
            return round(self.y[i[0]],4)
        if n==2:
            return round((self.y[i[1]]-self.y[i[0]])/(self.x[i[1]]-self.x[i[0]]),4)
        else:
            return round((self.g(i[1:])-self.g(i[:-1]))/(self.x[i[-1]]-self.x[i[0]]),4)
    
    def endless_delta(self):
        dy = []
        dy.append(self.y)
        while(len(dy[-1])!=1):
            ddy = []
            for i in range(len(dy[-1])-1):
                ddy.append((dy[-1][i+1]-dy[-1][i]))
            dy.append(ddy)
        self.endless = dy

    def N_not_same(self):
        N = [str(self.g([0]))]
        for i in range(1,self.n):
            coef = self.g(list(range(i+1)))
            l = [f"({coef})"]
            for j in range(i):
                l.append(f"(x-{self.x[j]})")
            N.append("*".join(l))
        return "+".join(N)


    def N_same(self):
        assert len(set([self.x[i]-self.x[i-1] for i in range(1,self.n)])) == 1, "dx must be the same for all i"
        self.endless_delta()
        dy = self.endless
        h = self.x[1]-self.x[0]
        N = [str(self.y[0])]
        for i in range(1,self.n):
            coef = round(dy[i][0]/(math.factorial(i)*h**i),4)
            l = [f"({coef})"]
            for j in range(i):
                l.append(f"(x-{self.x[j]})")
            N.append("*".join(l))
        return "+".join(N)
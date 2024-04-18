from math import sin, cos, tan, exp, log, sqrt, pi
def cot(x):
    return 1/tan(x)
def csc(x):
    return 1/sin(x)
def sec(x):
    return 1/cos(x)

from copy import deepcopy
import lab1.matrix as matrix
e = exp(1)


class Approximation:

    def __init__(self,table):
        assert len(table) == 2
        assert len(table[0]) == len(table[1])
        self.table = table



    def linear(self):
        n = len(self.table[0])
        sx = sum(self.table[0])
        sy = sum(self.table[1])
        sxy = sum([self.table[0][i]*self.table[1][i] for i in range(n)])
        sx2 = sum([self.table[0][i]**2 for i in range(n)])
        a = (n*sxy - sx*sy)/(n*sx2 - sx**2)
        b = (sy - a*sx)/n
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*self.table[0][i] - b)**2
        x_avg = sx/n
        y_avg = sy/n
        r_up = sum([(self.table[0][i] - x_avg)*(self.table[1][i] - y_avg) for i in range(n)])
        r_down = sqrt(sum([(self.table[0][i] - x_avg)**2 for i in range(n)])*sum([(self.table[1][i] - y_avg)**2 for i in range(n)]))
        delta = sqrt((sum([(a*self.table[0][i]+b-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,S,r_up/r_down,delta
    

    def square(self):
        n = len(self.table[0])
        sx = sum(self.table[0])
        sy = sum(self.table[1])
        sx2 = sum([self.table[0][i]**2 for i in range(n)])
        sx3 = sum([self.table[0][i]**3 for i in range(n)])
        sx4 = sum([self.table[0][i]**4 for i in range(n)])
        sy = sum(self.table[1])
        sxy = sum([self.table[0][i]*self.table[1][i] for i in range(n)])
        sx2y = sum([self.table[0][i]**2*self.table[1][i] for i in range(n)])
        rows = [[n,sx,sx2,sy],[sx,sx2,sx3,sxy],[sx2,sx3,sx4,sx2y]]
        m = matrix.Matrix(rows)
        m.triangular_matrix()
        solution = m.solve_system_gauss()
        a = solution[2]
        b = solution[1]
        c = solution[0]
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*self.table[0][i]**2 - b*self.table[0][i] - c)**2
        delta = sqrt((sum([(a*self.table[0][i]**2+b*self.table[0][i]+c-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,c,S,delta
    

    def qube(self):
        n = len(self.table[0])
        sx = sum(self.table[0])
        sy = sum(self.table[1])
        sx2 = sum([self.table[0][i]**2 for i in range(n)])
        sx3 = sum([self.table[0][i]**3 for i in range(n)])
        sx4 = sum([self.table[0][i]**4 for i in range(n)])
        sx5 = sum([self.table[0][i]**5 for i in range(n)])
        sx6 = sum([self.table[0][i]**6 for i in range(n)])
        sxy = sum([self.table[0][i]*self.table[1][i] for i in range(n)])
        sx2y = sum([self.table[0][i]**2*self.table[1][i] for i in range(n)])
        sx3y = sum([self.table[0][i]**3*self.table[1][i] for i in range(n)])
        rows = [[n,sx,sx2,sx3,sy],[sx,sx2,sx3,sx4,sxy],[sx2,sx3,sx4,sx5,sx2y],[sx3,sx4,sx5,sx6,sx3y]]
        m = matrix.Matrix(rows)
        m.triangular_matrix()
        solution = m.solve_system_gauss()
        a = solution[3]
        b = solution[2]
        c = solution[1]
        d = solution[0]
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*self.table[0][i]**3 - b*self.table[0][i]**2 - c*self.table[0][i] - d)**2
        delta = sqrt((sum([(a*self.table[0][i]**3+b*self.table[0][i]**2+c*self.table[0][i]+d-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,c,d,S,delta
    

    def axb(self):
        tables_old = deepcopy(self.table)
        n = len(self.table[0])
        for i in range(n):
            self.table[0][i] = log(self.table[0][i])
            self.table[1][i] = log(self.table[1][i])
        solution = self.linear()
        self.table = tables_old
        a = exp(solution[0])
        b = solution[1]
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*self.table[0][i]**b)**2
        delta = sqrt((sum([(a*self.table[0][i]**b-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,S,delta
    
    def aebx(self):
        tables_old = deepcopy(self.table)
        n = len(self.table[0])
        for i in range(n):
            self.table[1][i] = log(self.table[1][i])
        solution = self.linear()
        self.table = tables_old
        a = exp(solution[1])
        b = solution[0]
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*exp(b*self.table[0][i]))**2
        delta = sqrt((sum([(a*exp(b*self.table[0][i])-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,S,delta
    
    def alnxplusb(self):
        tables_old = deepcopy(self.table)
        n = len(self.table[0])
        for i in range(n):
            self.table[0][i] = log(self.table[0][i])
        solution = self.linear()
        self.table = tables_old
        a = solution[0]
        b = solution[1]
        S = 0
        for i in range(n):
            S += (self.table[1][i] - a*log(self.table[0][i]) - b)**2
        delta = sqrt((sum([(a*log(self.table[0][i])+b-self.table[1][i])**2 for i in range(n)]))/n)
        return a,b,S,delta


#_______________________________________________________________________________________________________________________
class Equation:
    @staticmethod
    def get_function(st):
        st = st.replace("^", "**")
        exec("def f(x): return" + st)
        #return f
        return lambda x: eval(st)
    @staticmethod
    def get_table(a,b,f,n):
        h = (b-a)/n
        table = [[],[]]
        for i in range(n+1):
            table[0].append(a+i*h)
            table[1].append(f(a+i*h))
        return table

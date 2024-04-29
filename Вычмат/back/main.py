from flask import Flask, request, jsonify
from flask_cors import CORS
import lab2.LinearEquation as le
import lab2.System as Sy
import lab3.Integrals as Int
import lab4.Approximation as Ap
import lab5.Interpolation as lab5
import math

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})



@app.route('/lab2/eq',methods=['POST'])
def solve_equation():
    try:
        data = request.get_json()
        a = data.get('a', 0)
        b = data.get('b', 0)
        e = data.get('e', 0)
        eq = int(data.get('eq', ""))
        m = data.get('m', "")
        l = le.Equations()
        l.check_for_roots(a,b,eq-1,0)
        if(m=="1"):
            return jsonify(l.binary_search(a, b, e, eq-1))
        elif(m=="2"):
            return jsonify(l.secant_method(a, b, e, eq-1))
        elif(m=="3"):
            return jsonify(l.simple_iteration(a, b, e, eq-1))
        else:
            return jsonify(error="Unavailable"), 400
    except(TimeoutError) as e:
        return jsonify(error=str(e)), 400
    except(ValueError) as e:
        return jsonify(error=str(e)), 400
    except(IndexError) as e:
        return jsonify(error=str(e)), 400
    except(SyntaxError) as e:
        return jsonify(error=str(e)), 400
    except(OverflowError) as e:
        return jsonify(error="I can't do with such small calculation"), 400
    except(ZeroDivisionError) as e:
        return jsonify(error="The derivative is zero, use another method"), 400

@app.route('/lab2/s',methods=['POST'])
def solve_system():
    try:
        data = request.get_json()
        a0 = data.get("a0",0)
        b0 =data.get("b0",0)
        a1 =data.get("a",0)
        b1 =data.get("b",0)
        e =data.get("e",0)
        eq = data.get('eq', "")
        s = Sy.System()
        return jsonify(s.Newton(a0,b0,a1,b1,e,eq))
    except(ValueError) as e:
        return jsonify(error=str(e)), 400
    except:
        return jsonify(error="An error occurred"), 400



@app.route('/lab3/int',methods=['POST'])
def solve_integral():
    try:
        data = request.get_json()
        a = data.get("a",0)
        b =data.get("b",0)
        equathion = data.get("eq", "")
        method = data.get("m", "")
        eps = data.get("e", "")
        integral = Int.Integrals(a,b,equathion,method,eps)
        answer = integral.solve()
        return jsonify(answer.__dict__)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except ZeroDivisionError as e:
        return jsonify(error="One of the partions is infinity, use another method to check for integral coverage"), 400
    except:
        return jsonify(error="An error occurred"), 400

@app.route('/lab4/app', methods=['POST'])
def solve_approximation():
    try:
        data = request.get_json()
        eq = data.get("eq", "")
        a = data.get("a", 0)
        b = data.get("b", 0)
        n = 12 #count of points
        f = Ap.Equation.get_function(eq)
        table = Ap.Equation.get_table(a,b,f,n)
        approx = Ap.Approximation(table)
        try:
            linear = approx.linear()
        except:
            linear = [None,None,None,None,None]
        try:
            square = approx.square()
            if(abs(square[0])<10**-6):
                raise ValueError("The approximation is too bad")
        except:
            square = [None,None,None,None,None]
        try:
            qube = approx.qube()
            if(abs(qube[0])<10**-6):
                raise ValueError("The approximation is too bad")
        except:
            qube = [None,None,None,None,None,None]
        try:
            axb = approx.axb()
        except:
            axb = [None,None,None,None,None]
        try:
            aebx = approx.aebx()
        except:
            aebx = [None,None,None,None,None]
        try:
            alnx = approx.alnxplusb()
        except:
            alnx = [None,None,None,None,None]
        #find the best approximation with the smallest delta
        f = None
        R2 = None
        if linear[4] is not None and (square[4] is None or linear[4] < square[4]) and (qube[5] is None or linear[4] < qube[5]) and (axb[3] is None or linear[4] < axb[3]) and (aebx[3] is None or linear[4] < aebx[3]) and (alnx[3] is None or linear[4] < alnx[3]):
            f = 1
            R2 = 1 - linear[2] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        elif square[4] is not None and (linear[4] is None or square[4] < linear[4]) and (qube[5] is None or square[4] < qube[5]) and (axb[3] is None or square[4] < axb[3]) and (aebx[3] is None or square[4] < aebx[3]) and (alnx[3] is None or square[4] < alnx[3]):
            f = 2
            R2 = 1 - square[3] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        elif qube[5] is not None and (linear[4] is None or qube[5] < linear[4]) and (square[4] is None or qube[5] < square[4]) and (axb[3] is None or qube[5] < axb[3]) and (aebx[3] is None or qube[5] < aebx[3]) and (alnx[3] is None or qube[5] < alnx[3]):
            f = 3
            R2 = 1 - qube[4] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        elif axb[3] is not None and (linear[4] is None or axb[3] < linear[4]) and (square[4] is None or axb[3] < square[4]) and (qube[5] is None or axb[3] < qube[5]) and (aebx[3] is None or axb[3] < aebx[3]) and (alnx[3] is None or axb[3] < alnx[3]):
            f = 4
            R2 = 1 - axb[2] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        elif aebx[3] is not None and (linear[4] is None or aebx[3] < linear[4]) and (square[4] is None or aebx[3] < square[4]) and (qube[5] is None or aebx[3] < qube[5]) and (axb[3] is None or aebx[3] < axb[3]) and (alnx[3] is None or aebx[3] < alnx[3]):
            f = 5
            R2 = 1 - aebx[2] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        elif alnx[3] is not None and (linear[4] is None or alnx[3] < linear[4]) and (square[4] is None or alnx[3] < square[4]) and (qube[5] is None or alnx[3] < qube[5]) and (axb[3] is None or alnx[3] < axb[3]) and (aebx[3] is None or alnx[3] < aebx[3]):
            f = 6
            R2 = 1 - alnx[2] / sum([(table[1][i] - sum(table[1]) / n) ** 2 for i in range(n)])
        sending = {
            "linear": {"a": linear[0], "b": linear[1], "S": linear[2], "r": linear[3], "delta": linear[4]},
            "square": {"a": square[0], "b": square[1], "c": square[2], "S": square[3], "delta": square[4]},
            "qube": {"a": qube[0], "b": qube[1], "c": qube[2], "d": qube[3], "S": qube[4], "delta": qube[5]},
            "axb": {"a": axb[0], "b": axb[1], "S": axb[2], "delta": axb[3]},
            "aebx": {"a": aebx[0], "b": aebx[1], "S": aebx[2], "delta": aebx[3]},
            "alnx": {"a": alnx[0], "b": alnx[1], "S": alnx[2], "delta": alnx[3]},
            "R2": R2,
            "f": f
        }
        return jsonify(sending)
    except SyntaxError as e:
        return jsonify(error="enter correct function"), 400


@app.route('/lab5', methods=['POST'])
def solve_interpolation():
    try:
        data = request.get_json()
        m = data.get("m", False)
        if(m):
            x = data.get("x", [])
            y = data.get("y", [])
            x_ = data.get("x_", [])
        else:
            file = "./back/"+data.get("file", "")
            x = []
            y = []
            x_ = 0
            try:
                with open(file, "r") as f:
                    x = list(map(float, f.readline().split()))
                    y = list(map(float, f.readline().split())) 
                    x_ = float(f.readline())
            except:
                return jsonify(error="File not found"), 400
        interpolation = lab5.Interpolation(x, y)
        lagrange = interpolation.L().replace("--", "+")
        newton_same = None
        try:
            newton_same = interpolation.N_same().replace("--", "+")
        except AssertionError as e:
            newton_same = None
        newton_not_same = interpolation.N_not_same().replace("--", "+")
        x1_ = eval(lagrange.replace("x", "("+str(x_)+")"))
        x2_ = eval(newton_not_same.replace("x", "("+str(x_)+")"))
        if newton_same is not None:
            x3_ = eval(newton_same.replace("x", "("+str(x_)+")"))
        else:
            x3_ = "Cannot use this method for this point"
        sending = {
            "x1": x1_,
            "x2": x2_,
            "x3": x3_,
            "func1": lagrange,
            "func2": newton_not_same,
            "func3": newton_same,
            "x": x,
            "y": y,
            "dy": interpolation.endless
        }
        return jsonify(sending)
    except AssertionError as e:
        return jsonify(error=str(e)), 400
    
   
    

if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify
from flask_cors import CORS
import lab2.LinearEquation as le
import lab2.System as Sy
import lab3.Integrals as Int

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



if __name__ == '__main__':
    #st = "def f(x): return x**2"
    #exec(st)
    app.run()
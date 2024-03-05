from flask import Flask, request, jsonify
from flask_cors import CORS
import lab2.LinearEquation as le
app = Flask(__name__)
CORS(app, resources={r"/lab2/eq": {"origins": "http://localhost:5173"}})


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

if __name__ == '__main__':
    app.run()
import React, { useState } from "react";
import { Alerts } from "../general/subs/Alert";
import Graph from "./subs/Graph";
import ButtonSubmit from "../general/subs/ButtonSubmit";
import RadioMethodInterpolation from "./subs/RadioMethodInterpolation";
import InputInterpolation from "./subs/InputInterpolation";

const Interpolation = () => {
  const [err, setErr] = useState("");
  const [m, setM] = useState("1");
  const [lagrange, setLagrange] = useState(null);
  const [newton, setNewton] = useState(null);
  const [newton2, setNewton2] = useState(null);
  const [x, setX] = useState(null);
  const [y, setY] = useState(null);
  const [file, setFile] = useState(null);
  const [a, setA] = useState(null);
  const [b, setB] = useState(null);
  const [n, setN] = useState(null);
  const [x_find, setXfind] = useState(null);
  const [x_array, setX_array] = useState<number[] | null>(null);
  const [y_array, setY_array] = useState<number[] | null>(null);
  const [res1, setRes1] = useState(null);
  const [res2, setRes2] = useState(null);
  const [res3, setRes3] = useState(null);
  const [dy, setDy] = useState(null);
  const handleClick = async (e) => {
    e.preventDefault();
    let data = {};
    if (m == "1") {
      if (!x || !y || !x_find) {
        setErr("Please enter x and y values");
        return;
      }
      let xx = x.toString().replace(",", ".");
      let yy = y.toString().replace(",", ".");
      let x_find1 = x_find.toString().replace(",", ".");
      if(isNaN(parseFloat(x_find1))){
        setErr("Please enter a valid number");
        return;
      }
      let x_find2 = parseFloat(x_find1);
      let xx1 = xx.split(" ");
      let yy1 = yy.split(" ");
      let x1 = [];
      let y1 = [];
      for (let i = 0; i < xx1.length; i++) {
        if (isNaN(parseFloat(xx1[i])) || isNaN(parseFloat(yy1[i]))) {
          setErr("Please check if every number is valid");
          return;
        }
        x1.push(parseFloat(xx1[i]));
        y1.push(parseFloat(yy1[i]));
      }
      data = {
        x: x1,
        y: y1,
        x_: x_find2,
        m: true,
      };
    } else if (m == "2") {
      if (!file) {
        setErr("Please enter a filename");
        return;
      }
      data = {
        file: file,
        m: false,
      };
    } else if (m == "3") {
      console.log(a, b, n, x_find);
      if (!a || !b || !n || !x_find) {
        setErr("Please enter a, b and n values");
        return;
      }
      let x_find1 = x_find.toString().replace(",", ".");
      let aa = a.toString().replace(",", ".");
      let bb = b.toString().replace(",", ".");
      let nn = n.toString().replace(",", ".");
      if (isNaN(aa) || isNaN(bb) || isNaN(nn) || isNaN(x_find)) {
        setErr("Please enter a valid number");
        return;
      }
      let x_find2 = parseFloat(x_find1);
      let a1 = parseFloat(aa);
      let b1 = parseFloat(bb);
      let n1 = parseInt(nn);
      let h = (b1 - a1) / n1;
      let x1 = [];
      let y1 = [];
      for (let i = 0; i <= n1; i++) {
        x1.push(parseFloat((a1 + i * h).toFixed(4)));
        y1.push(parseFloat(Math.sin(a1 + i * h).toFixed(4)));
      }
      data = {
        x: x1,
        y: y1,
        x_: x_find2,
        m: true,
      };
    } else {
      console.log(a, b, n, x_find);
      if (!a || !b || !n || !x_find) {
        setErr("Please enter a, b and n values");
        return;
      }
      let aa = a.toString().replace(",", ".");
      let bb = b.toString().replace(",", ".");
      let nn = n.toString().replace(",", ".");
      if (isNaN(aa) || isNaN(bb) || isNaN(nn) || isNaN(x_find)) {
        setErr("Please enter a valid number");
        return;
      }
      let x2 = [];
      let y2 = [];
      let x_find1 = x_find.toString().replace(",", ".");
      let x_find2 = parseFloat(x_find1);
      let a1 = parseFloat(aa);
      let b1 = parseFloat(bb);
      let n1 = parseInt(nn);
      let h = (b1 - a1) / n1;
      for (let i = 0; i <= n1; i++) {
        x2.push(parseFloat((a1 + i * h).toFixed(4)));
        y2.push(parseFloat(Math.exp(a1 + i * h).toFixed(4)));
      }
      data = {
        x: x2,
        y: y2,
        x_: x_find2,
        m: true,
      };
    }
    setErr("");
    try {
      const response = await fetch("http://localhost:5000/lab5", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setLagrange(result.func1);
        setNewton(result.func2);
        setNewton2(result.func3);
        setX_array(result.x);
        setY_array(result.y);
        setRes1(result.x1);
        setRes2(result.x2);
        setRes3(result.x3);
        setDy(result.dy);
      } else {
        const errr = await response.text();
        setErr(errr.toString().replace('{"error":"', "").replace('"}', ""));
      }
    } catch (error) {
      setErr("Fetch (SERVER) error:" + error);
    }
  };
  return (
    <div>
      <h2>Interpolation</h2>
      <div className="flex row fullwidth">
        <div className="flex halfscreen column">
          <form onSubmit={handleClick}>
            <RadioMethodInterpolation
              value={m}
              setValue={setM}
            ></RadioMethodInterpolation>
            <InputInterpolation
              m={m}
              setA={setA}
              setB={setB}
              setFile={setFile}
              setN={setN}
              setX={setX}
              setY={setY}
              setXfind={setXfind}
            ></InputInterpolation>
            <ButtonSubmit></ButtonSubmit>
            {err && <Alerts message={err} />}
          </form>
        </div>
        <div className="halfscreen flex column">
          <Graph
            lagr={lagrange}
            newt1={newton}
            newt2={newton2}
            x1={x_array}
            y1={y_array}
          />
        </div>
        <div className="halfscreen flex column">
          {res1 && (
            <h3>Lagrange polinomal (x*): {res1}</h3>
            )}
          {res2 && (
            <h3>Newton polinomal (diff) (x*): {res2}</h3>
            )}
          {res3 && (
            <h3>Newton polinomal (same) (x*): {res3}</h3>
            )}
            {dy && (
              <div className="flex column">
                <h3>Diff. table:</h3>
                <table>
                  <tbody>
                    {dy.map((row, rowIndex) => (
                      <tr key={rowIndex}>
                        {row.map((value, colIndex) => (
                          <td key={colIndex}>{value}</td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
        </div>
      </div>
    </div>
  );
};

export default Interpolation;

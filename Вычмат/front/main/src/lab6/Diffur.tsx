import React, { useState } from "react";
import { Alerts } from "../general/subs/Alert";
import Graph from "./subs/Graph";
import ButtonSubmit from "../general/subs/ButtonSubmit";
import InputDiff from "./subs/InputDiff";
import RadioMethodDiff from "./subs/RadioMethodDiff";
import RadioFunctionDiff from "./subs/RadioFunctionDiff";

const Integrals = () => {
  const [eq, setValue] = React.useState("1");
  const [xn, setB] = useState(null);
  const [ee, setE] = useState(null);
  const [m, setM] = useState("1");
  const [err, setErr] = useState("");
  const [x, setX] = useState<number | null>(null);
  const [y, setY] = useState<number | null>(null);
  const [c, setC] = useState(null);
  const [x0, setX0] = useState(null);
  const [y0, setY0] = useState(null);
  const handleClick = async (e) => {
    e.preventDefault();
    if (xn === null || ee === null || x0 === null || y0 === null) {
      setErr("Please fill all the fields");
      return;
    }
    let xn1 = xn.toString().replace(",", ".");
    let e1 = ee.toString().replace(",", ".");
    let x01 = x0.toString().replace(",", ".");
    let y01 = y0.toString().replace(",", ".");
    let eqq = parseInt(eq);
    let mm = parseInt(m);
    if (isNaN(xn1) || isNaN(e1) || isNaN(x01) || isNaN(y01)) {
      setErr("Please enter a valid number");
      return;
    }
    setErr("");
    const data = {
      xn: parseFloat(xn1),
      e: parseFloat(e1),
      eq: eqq,
      m: mm,
      x0: parseFloat(x01),
      y0: parseFloat(y01),
    };
    try {
      const response = await fetch("http://localhost:5000/lab6", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setX(result.x);
        setY(result.y);
        setC(result.c);
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
      <h2>Diff. equathion</h2>
      <div className="flex row fullwidth">
        <div className="flex halfwidth marg-right marg-left column">
          <form onSubmit={handleClick} className="flex column">
            <RadioFunctionDiff
              setC={setC}
              setX={setX}
              setY={setY}
              value={eq}
              setValue={setValue}
            ></RadioFunctionDiff>
            <RadioMethodDiff
              setC={setC}
              setX={setX}
              setY={setY}
              value={m}
              setValue={setM}
            ></RadioMethodDiff>
            <InputDiff
              ee={ee}
              x0={x0}
              y0={y0}
              setX0={setX0}
              setY0={setY0}
              setE={setE}
              xn={xn}
              setXN={setB}
            ></InputDiff>
            <ButtonSubmit></ButtonSubmit>
            {err && <Alerts message={err} />}
          </form>
        </div>
        <div className="realhalf flex column">
          <Graph eq={eq} c={c} xx={x} yy={y} />
        </div>
      </div>
    </div>
  );
};

export default Integrals;

import React, { useState } from "react";
import { Alerts } from "./subs/Alert";
import ButtonSubmit from "./subs/ButtonSubmit";
import InputLinear from "./subs/InputLinear";
import RadioButtonsSystem from "./subs/NLSystem";
import RadioMethodS from "./subs/RadioMethodS";
import GraphS from "./subs/GraphS";


const LSystem = () => {
  const [eq, setValue] = React.useState("1");
  const [a, setA] = useState(null);
  const [b, setB] = useState(null);
  const [ee, setE] = useState(null);
  const [resultx, setResultx] = useState(null);
  const [resultf, setResultf] = useState(null);
  const [resultk, setResultk] = useState(null);
  const [m, setM] = useState("1");
  const [err, setErr] = useState("");
  const handleClick = async (e) => {
    e.preventDefault();
    if (a === null || b === null || ee === null) {
      setErr("Please fill all the fields");
      return;
    }
    let a1 = a.toString().replace(",", ".");
    let b1 = b.toString().replace(",", ".");
    let e1 = ee.toString().replace(",", ".");
    console.log(a1, b1, e1);
    if (isNaN(a1) || isNaN(b1) || isNaN(e1)) {
      setErr("Please enter a valid number");
      return;
    }
    setErr("");
    const data = {
      a: parseFloat(a1),
      b: parseFloat(b1),
      e: parseFloat(e1),
      eq: eq,
      m: m,
    };
    try {
      const response = await fetch("http://localhost:5000/lab2/eq", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setResultx(result.x);
        setResultf(result.f);
        setResultk(result.k);
      } else {
        const errr = await response.text();
        setErr(errr.toString().replace("{\"error\"\:\"","").replace("\"}",""));
      }
    } catch (error) {
      setErr("Fetch error:" + error);
    }
  };
  return (
    <div>
      <h2>Non linear system</h2>
      <div className="flex row fullwidth">
        <div className="flex halfscreen column">
          <RadioButtonsSystem value={eq} setValue={setValue} />
          <RadioMethodS value={m} setValue={setM} />
        </div>
        <div className="halfscreen flex column">
          <GraphS eq={eq}></GraphS>
          <form onSubmit={handleClick}>
            <InputLinear
              method={m}
              a={a}
              b={b}
              ee={ee}
              setA={setA}
              setB={setB}
              setE={setE}
            />
            {err && <Alerts message={err} />}
            <ButtonSubmit></ButtonSubmit>
          </form>
        </div>
        <div className="halfscreen">
          {resultx && <h3>X value: {resultx}</h3>}
          {resultf && <h3>F(x): {resultf}</h3>}
          {(resultk||resultx) && <h3>Iteration count: {resultk}</h3>}
        </div>
      </div>
    </div>
  );
};

export default LSystem;

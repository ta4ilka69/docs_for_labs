import React, { useState } from "react";
import { Alerts } from "../general/subs/Alert";
import ButtonSubmit from "../general/subs/ButtonSubmit";
import RadioButtonsSystem from "./subs/NLSystem";
import RadioMethodS from "./subs/RadioMethodS";
import GraphS from "./subs/GraphS";
import InputSystem from "./subs/InputSystem";


const LSystem = () => {
  const [eq, setValue] = React.useState("1");
  const [a, setA] = useState(null);
  const [b, setB] = useState(null);
  const [ee, setE] = useState(null);
  const [a0, setA0] = useState(null);
  const [b0, setB0] = useState(null)
  const [err, setErr] = useState("");
  const [resultX, setResultX] = useState(null);
  const [resultK, setResultK] = useState(null);
  const [resultY, setResultY] = useState(null);
  const handleClick = async (e) => {
    e.preventDefault();
    if (a === null || b === null || ee === null||a0===null||b0===null) {
      setErr("Please fill all the fields");
      return;
    }
    let a1 = a.toString().replace(",", ".");
    let b1 = b.toString().replace(",", ".");
    let e1 = ee.toString().replace(",", ".");
    let a2 = a0.toString().replace(",", ".");
    let b2 = b0.toString().replace(",", ".");
    console.log(a1, b1, e1);
    if (isNaN(a1) || isNaN(b1) || isNaN(e1) || isNaN(a2) || isNaN(b2)){
      setErr("Please enter a valid number");
      return;
    }
    setErr("");
    const data = {
      a: parseFloat(a1),
      b: parseFloat(b1),
      e: parseFloat(e1),
      eq: eq,
      a0: parseFloat(a2),
      b0: parseFloat(b2),
    };
    try {
      const response = await fetch("http://localhost:5000/lab2/s", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setResultX(result.x);
        setResultK(result.k);
        setResultY(result.y);
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
          <RadioMethodS />
        </div>
        <div className="halfscreen flex column">
          <GraphS eq={eq}></GraphS>
          <form onSubmit={handleClick}>
            <InputSystem
              a={a}
              b={b}
              ee={ee}
              setA={setA}
              setB={setB}
              setE={setE}
              a0 = {a0}
              setA0 = {setA0}
              b0 = {b0}
              setB0 = {setB0}
            />
            {err && <Alerts message={err} />}
            <ButtonSubmit></ButtonSubmit>
          </form>
        </div>
        <div className="halfscreen">
          {resultX && <h3>X value: {resultX}</h3>}
          {(resultK||resultX) && <h3>Iteration count: {resultK}</h3>}
          {resultY && <h3>Y value: {resultY}</h3>}
        </div>
      </div>
    </div>
  );
};

export default LSystem;

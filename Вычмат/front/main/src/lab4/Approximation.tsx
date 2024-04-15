import React, { useState } from "react";
import { Alerts } from "../general/subs/Alert";
import Graph from "./subs/Graph";
import ButtonSubmit from "../general/subs/ButtonSubmit";

const Approximation = () => {
  const [eq, setValue] = React.useState("");
  const [a, setA] = useState(null);
  const [b, setB] = useState(null);
  const [ee, setE] = useState(null);
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
    let eqq = parseInt(eq);
    let mm = parseInt(m);
    console.log(a1, b1, e1, eqq, mm);
    if (isNaN(a1) || isNaN(b1) || isNaN(e1)) {
      setErr("Please enter a valid number");
      return;
    }
    setErr("");
    const data = {
      a: parseFloat(a1),
      b: parseFloat(b1),
      e: parseFloat(e1),
      eq: eqq,
      m: mm,
    };
    try {
      const response = await fetch("http://localhost:5000/lab3/int", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setResultf(result.integral);
        setResultk(result.partions);
      } else {
        const errr = await response.text();
        setErr(errr.toString().replace("{\"error\"\:\"","").replace("\"}",""));
      }
    } catch (error) {
      setErr("Fetch (SERVER) error:" + error);
    }
  };
  return (
    <div>
      <h2>Integrals</h2>
      <div className="flex row fullwidth">
        <div className="flex halfscreen column">
        </div>
        <div className="halfscreen flex column">
          <form onSubmit={handleClick}>
            <Graph eq={eq} />
            <ButtonSubmit></ButtonSubmit>
            {err && <Alerts message={err} />}
          </form>
        </div>
        <div className="halfscreen">
        </div>
      </div>
    </div>
  );
};

export default Approximation;

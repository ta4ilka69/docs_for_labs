import React, { useState } from "react";
import { Alerts } from "../general/subs/Alert";
import Graph from "./subs/Graph";
import ButtonSubmit from "../general/subs/ButtonSubmit";
import InputFunction from "./subs/InputFunction";
import FunctionList from "./subs/FunctionList";

const Approximation = () => {
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(0);
  const [a1, setA1] = useState(null);
  const [b1, setB1] = useState(null);
  const [a2, setA2] = useState(null);
  const [b2, setB2] = useState(null);
  const [c2, setC2] = useState(null);
  const [a3, setA3] = useState(null);
  const [b3, setB3] = useState(null);
  const [c3, setC3] = useState(null);
  const [d3, setD3] = useState(null);
  const [a4, setA4] = useState(null);
  const [b4, setB4] = useState(null);
  const [a5, setA5] = useState(null);
  const [b5, setB5] = useState(null);
  const [a6, setA6] = useState(null);
  const [b6, setB6] = useState(null);
  const [eq, setEq] = useState("0");
  const [err, setErr] = useState("");
  const [r2, setR2] = useState(null);
  const [de1, setDe1] = useState(null);
  const [de2, setDe2] = useState(null);
  const [de3, setDe3] = useState(null);
  const [de4, setDe4] = useState(null);
  const [de5, setDe5] = useState(null);
  const [de6, setDe6] = useState(null);
  const [S1, setS1] = useState(null);
  const [S2, setS2] = useState(null);
  const [S3, setS3] = useState(null);
  const [S4, setS4] = useState(null);
  const [S5, setS5] = useState(null);
  const [S6, setS6] = useState(null);
  const [f, setF] = useState(null);
  const handleClick = async (e) => {
    e.preventDefault();
    if (eq === null || start === null || end === null) {
      setErr("Please fill all the fields");
      return;
    }
    if (isNaN(start) || isNaN(end)) {
      setErr("Please enter a valid number");
      return;
    }
    setErr("");
    const data = {
      eq: eq,
      a: parseFloat(start),
      b: parseFloat(end),
    };
    try {
      const response = await fetch("http://localhost:5000/lab4/app", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const result = await response.json();
        setA1(result.linear.a);
        setB1(result.linear.b);
        setA2(result.square.a);
        setB2(result.square.b);
        setC2(result.square.c);
        setA3(result.qube.a);
        setB3(result.qube.b);
        setC3(result.qube.c);
        setD3(result.qube.d);
        setA4(result.axb.a);
        setB4(result.axb.b);
        setA5(result.aebx.a);
        setB5(result.aebx.b);
        setA6(result.alnx.a);
        setB6(result.alnx.b);
        setR2(result.R2);
        setS1(result.linear.S);
        setS2(result.square.S);
        setS3(result.qube.S);
        setS4(result.axb.S);
        setS5(result.aebx.S);
        setS6(result.alnx.S);
        setDe1(result.linear.delta);
        setDe2(result.square.delta);
        setDe3(result.qube.delta);
        setDe4(result.axb.delta);
        setDe5(result.aebx.delta);
        setDe6(result.alnx.delta);
        setF(result.f);
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
      <h2>Approximation</h2>
      <div className="flex row fullwidth">
        <div className="flex smaller column">
          <form onSubmit={handleClick}>
            <InputFunction
              f={eq}
              setF={setEq}
              a={start}
              setA={setStart}
              b={end}
              setB={setEnd}
            />
            <ButtonSubmit></ButtonSubmit>
            {err && <Alerts message={err} />}
          </form>
        </div>
        <div className="smaller flex column">
          <form onSubmit={handleClick}>
            <Graph
              a1={a1}
              b1={b1}
              a2={a2}
              b2={b2}
              c2={c2}
              a3={a3}
              b3={b3}
              c3={c3}
              d3={d3}
              a4={a4}
              b4={b4}
              a5={a5}
              b5={b5}
              a6={a6}
              b6={b6}
            />
          </form>
        </div>
        <div className="halfscreen marg-left">
          {f && <h3>Function № {f}</h3>}
          {r2 && <h3>R = {r2}</h3>}
          <FunctionList
            a1={a1}
            b1={b1}
            a2={a2}
            b2={b2}
            c2={c2}
            a3={a3}
            b3={b3}
            c3={c3}
            d3={d3}
            a4={a4}
            b4={b4}
            a5={a5}
            b5={b5}
            a6={a6}
            b6={b6}
            de1={de1}
            de2={de2}
            de3={de3}
            de4={de4}
            de5={de5}
            de6={de6}
            S1={S1}
            S2={S2}
            S3={S3}
            S4={S4}
            S5={S5}
            S6={S6}
          ></FunctionList>
        </div>
      </div>
    </div>
  );
};

export default Approximation;

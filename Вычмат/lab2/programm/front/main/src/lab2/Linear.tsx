import React, { useState } from "react";
import RadioButtonsGroup from "./subs/RadioEquations";
import RadioMethodsL from "./subs/RadioMethodL";
import Graph from "./subs/Graph";

const Linear = () => {
  const [eq, setValue] = React.useState("1");
  const [a, setA] = useState(0);
  const [b, setB] = useState(0);
  const [e, setE] = useState(0);
  const [m, setM] = useState("1");
  return (
    <div>
      <h2>Non linear equation</h2>
      <div className="flex row fullwidth">
        <div className="flex halfscreen column">
          <RadioButtonsGroup value={eq} setValue={setValue} />
          <RadioMethodsL value={m} setValue={setM} />
        </div>
        <div className="halfscreen flex column">
          <Graph eq = {eq}></Graph>
          <p></p>
          
        </div>
        <div className="halfscreen">

        </div>
      </div>
    </div>
  );
};

export default Linear;

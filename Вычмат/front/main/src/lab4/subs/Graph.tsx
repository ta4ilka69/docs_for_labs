import { Mafs, Coordinates, Plot, Theme } from "mafs";
import React from "react";

export default function Graph({
  a1,
  b1,
  a2,
  b2,
  c2,
  a3,
  b3,
  c3,
  d3,
  a4,
  b4,
  a5,
  b5,
  a6,
  b6,
}) {
  let f1 = (x: number) => a1 * x + b1;
  let f2 = (x: number) => a2 * x * x + b2 * x + c2;
  let f3 = (x: number) => a3 * x * x * x + b3 * x * x + c3 * x + d3;
  let f4 = (x: number) => a4 * Math.pow(x, b4);
  let f5 = (x: number) => a5 * Math.pow(Math.E, b5 * x);
  let f6 = (x: number) => a6 * Math.log(x) + b6;

  return (
    <Mafs zoom={{ min: 0.3, max: 4 }}>
      <Coordinates.Cartesian subdivisions={10} />
      {a1 !== null && b1 !== null && <Plot.OfX y={f1} color={Theme.yellow} minSamplingDepth={12} />}
      {a2 !== null && b2 !== null && c2 !== null && <Plot.OfX y={f2} color={Theme.blue} minSamplingDepth={12} />}
      {a3 !== null && b3 !== null && c3 !== null && d3 !== null && <Plot.OfX y={f3} color={Theme.orange} minSamplingDepth={12} />}
      {a4 !== null && b4 !== null && <Plot.OfX y={f4} color={Theme.red} minSamplingDepth={12} />}
      {a5 !== null && b5 !== null && <Plot.OfX y={f5} color={Theme.pink} minSamplingDepth={12} />}
      {a6 !== null && b6 !== null && <Plot.OfX y={f6} color={Theme.green} minSamplingDepth={12} />}
    </Mafs>
  );
}

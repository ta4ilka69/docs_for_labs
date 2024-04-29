import { Mafs, Coordinates, Plot, Theme, Point } from "mafs";
import React from "react";
export default function Graph({ lagr, newt1, newt2, x1, y1 }) {
  const f = lagr !== null ? (x) => eval(lagr) : null;
  const g = newt1 !== null ? (x) => eval(newt1) : null;
  const g1 = newt2 !== null ? (x) => eval(newt2) : null;
  return (
    <Mafs zoom={{ min: 0.3, max: 4 }}>
      <Coordinates.Cartesian subdivisions={10} />
      {f && <Plot.OfX y={f} color={Theme.yellow} minSamplingDepth={12} />}
      {g && <Plot.OfX y={g} color={Theme.blue} minSamplingDepth={12} />}
      {g1 && <Plot.OfX y={g1} color={Theme.red} minSamplingDepth={12} />}
      {x1 !== null &&
        y1 !== null &&
        x1.length === y1.length &&
        x1.map((x, i) => <Point x={x} y={y1[i]} color={Theme.green} />)}
    </Mafs>
  );
}

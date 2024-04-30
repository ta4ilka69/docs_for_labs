import { Mafs, Coordinates, Plot, Theme, Point } from "mafs";
import React from "react";
export default function Graph({ eq, c, xx, yy }) {
  let f;
  if (c !== null) {
    if (eq === "1") {
      f = (x: number) => -Math.exp(x) / (c + Math.exp(x) * x);
    } else if (eq === "2") {
      f = (x: number) => c * Math.exp(x) + x + 1;
    } else {
      f = (x: number) => c * Math.exp(-x) + Math.exp(x) / 2;
    }
  }
  return (
    <Mafs height={800} zoom={{ min: 0.2, max: 5}}>
      <Coordinates.Cartesian subdivisions={10} />
      {f !== undefined && (
        <Plot.OfX y={f} color={Theme.yellow} minSamplingDepth={12} />
      )}
      {xx !== null &&
        yy !== null &&
        xx.map((x, i) => <Point key={i} x={x} y={yy[i]} color={Theme.red} />)}
    </Mafs>
  );
}

import { Mafs, Coordinates, Plot, Theme } from "mafs"
import React from "react";
export default function Graph({ eq }) {
    let f;
    if(eq === "1"){
        f = (x:number) => x**2-3*x+1;
    }
    else if(eq === "2"){
        f = (x:number) => Math.exp(x)-Math.sin(x)+x;
    }
    else if(eq === "3"){
        f = (x:number) => 1/Math.sin(x)+x**2;
    }
    else{
        f = (x:number) => 3/x**2-10/x+Math.exp(x)/10;
    }
  return (
    <Mafs zoom={{ min: 0.3, max: 4 }} >
      <Coordinates.Cartesian subdivisions={10}/>
      <Plot.OfX y={f} color={Theme.yellow} minSamplingDepth={14}/>
    </Mafs>
  );
}

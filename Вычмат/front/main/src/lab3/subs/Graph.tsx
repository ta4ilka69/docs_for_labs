import { Mafs, Coordinates, Plot, Theme } from "mafs"
import React from "react";
export default function Graph({ eq }) {
    let f;
    if(eq === "1"){
        f = (x:number) => (x-1)*(x-1);
    }
    else if(eq === "2"){
        f = (x:number) => Math.sin(Math.PI*x)/2;
    }
    else if(eq === "3"){
        f = (x:number) => Math.sqrt(x)/(Math.exp(x)-1)
    }
    else if(eq=="4"){
        f = (x:number) => Math.cos(Math.PI*x)-Math.exp(Math.sin(Math.PI*x))+1;
    }
    else{
        f = (x:number) => 1/(x*x-3*x+2);
    }
  return (
    <Mafs zoom={{ min: 0.3, max: 4 }} >
      <Coordinates.Cartesian subdivisions={10}/>
      <Plot.OfX y={f} color={Theme.yellow} minSamplingDepth={12}/>
    </Mafs>
  );
}

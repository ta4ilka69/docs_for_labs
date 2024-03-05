import { Mafs, Coordinates, Plot, Theme } from "mafs"
import React from "react";
export default function Graph({ eq }) {
    let f,g;
    if(eq === "1"){
        f = (x:number) => (-1/(Math.tan(x))-3)/2;
        g = (y:number) => 1-Math.tan(y);
    }
    else if(eq === "2"){
        f = (x:number) => -Math.exp(x)+5
        g = (y:number) => Math.log(y)-3
    }
    else{
        f = (x:number) => (Math.cos(4*x)-4)/2;
        g = (y:number) => (Math.sin(2*y)-1)/5
    }
  return (
    <Mafs zoom={{ min: 0.3, max: 4 }} >
      <Coordinates.Cartesian subdivisions={10}/>
      <Plot.OfX y={f} color={Theme.yellow} minSamplingDepth={12}/>
        <Plot.OfY x={g} color={Theme.green} minSamplingDepth={12}/>
    </Mafs>
  );
}

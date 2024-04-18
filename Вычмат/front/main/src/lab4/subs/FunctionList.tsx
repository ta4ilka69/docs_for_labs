import * as React from "react";
import FormControlLabel from "@mui/material/FormControlLabel";
import { LaTeX, Mafs } from "mafs";

export default function FunctionList({
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
  S1,
  S2,
  S3,
  S4,
  S5,
  S6,
  de1,
  de2,
  de3,
  de4,
  de5,
  de6,
  kor
}) {
  return (
    <div className="flex column center_items">
      {a1 != null && b1 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="1" control={<div />} label="1" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{yellow}{${a1.toFixed(
                  4
                )}x + ${b1.toFixed(4)}}`}
              />
            </Mafs>
          }
          {de1 != null && <h4>d: {de1.toFixed(4)}</h4>}
          {S1 != null && <h4>S: {S1.toFixed(4)}</h4>}
          {kor != null && <h4>r: {kor.toFixed(4)}</h4>}
        </div>
      )}
      {a2 != null && b2 != null && c2 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="2" control={<div />} label="2" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{blue}{${a2.toFixed(
                  4
                )}x^2 + ${b2.toFixed(4)}x + ${c2.toFixed(4)}}`}
              />
            </Mafs>
          }
          {de2 != null && <h4>d: {de2.toFixed(4)}</h4>}
          {S2 != null && <h4>S {S2.toFixed(4)}</h4>}
          
        </div>
      )}
      {a3 != null && b3 != null && c3 != null && d3 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="3" control={<div />} label="3" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{orange}{${a3.toFixed(
                  3
                )}x^3 + ${b3.toFixed(3)}x^2 + ${c3.toFixed(3)}x + ${d3.toFixed(
                  3
                )}}`}
              />
            </Mafs>
          }
          {de3 != null && <h4>d: {de3.toFixed(4)}</h4>}
          {S3 != null && <h4>S: {S3.toFixed(4)}</h4>}
        </div>
      )}
      {a4 != null && b4 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="4" control={<div />} label="4" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{red}{${a4.toFixed(4)}x^{${b4.toFixed(
                  4
                )}}}`}
              />
            </Mafs>
          }
          {de4 != null && <h4>d: {de4.toFixed(4)}</h4>}
          {S4 != null && <h4>S: {S4.toFixed(4)}</h4>}
        </div>
      )}
      {a5 != null && b5 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="5" control={<div />} label="5" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{magenta}{${a5.toFixed(
                  4
                )}e^{${b5.toFixed(4)}x}}`}
              />
            </Mafs>
          }
          {de5 != null && <h4>d: {de5.toFixed(4)}</h4>}
          {S5 != null && <h4>S: {S5.toFixed(4)}</h4>}
        </div>
      )}

      {a6 != null && b6 != null && (
        <div className="flex radiolinear center_self">
          <FormControlLabel value="6" control={<div />} label="6" />{" "}
          {
            <Mafs width={600} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\textcolor{green}{${a6.toFixed(
                  4
                )}\ln{x} + ${b6.toFixed(4)}}`}
              />
            </Mafs>
          }
          {de6 != null && <h4>d: {de6.toFixed(4)}</h4>}
          {S6 != null && <h4>S: {S6.toFixed(4)}</h4>}
        </div>
      )}
    </div>
  );
}

import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import { LaTeX, Mafs } from "mafs";

export default function RadioButtonsGroup({ value, setValue }) {
  return (
    <FormControl>
      <FormLabel
        sx={{ marginBottom: "3vh" }}
        id="demo-radio-buttons-group-label"
      >
        Equations
      </FormLabel>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="1"
        name="radio-buttons-group"
        value={value}
        onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
          setValue(event.target.value);
        }}
      >
        <div className="flex radiolinear center_self">
          <FormControlLabel value="1" control={<Radio />} label="" />{" "}
          {
            <Mafs width={300} height={50} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`x^2-3x+1`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="2" control={<Radio />} label="" />{" "}
          {
            <Mafs width={300} height={50} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`e^x-\sin{x}+x`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="3" control={<Radio />} label="" />{" "}
          {
            <Mafs width={300} height={50} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\frac{1}{\sin{x}}+x^2`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="4" control={<Radio />} label="" />{" "}
          {
            <Mafs width={300} height={50} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\frac{3}{x^2}-\frac{10}{x}+\frac{e^x}{10}`}
              />
            </Mafs>
          }
        </div>
      </RadioGroup>
    </FormControl>
  );
}

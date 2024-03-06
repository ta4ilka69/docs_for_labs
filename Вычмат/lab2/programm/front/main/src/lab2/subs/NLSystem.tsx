import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import { LaTeX, Mafs } from "mafs";

export default function RadioButtonsSystem({ value, setValue }) {
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
            <Mafs width={300} height={110} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\begin{cases} x+\tan{y}=1 \\ \cot{x}+2y=-3 \end{cases}`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="2" control={<Radio />} label="" />{" "}
          {
            <Mafs width={300} height={110} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\begin{cases} y+e^x=5 \\ \ln{y}-x=3 \end{cases}`} />
            </Mafs>
          }
        </div>
      </RadioGroup>
    </FormControl>
  );
}

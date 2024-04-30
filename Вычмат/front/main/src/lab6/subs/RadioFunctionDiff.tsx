import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import { LaTeX, Mafs } from "mafs";

export default function RadioFunctionDiff({
  value,
  setValue,
  setX,
  setY,
  setC,
}) {
  return (
    <FormControl>
      <FormLabel
        sx={{ marginBottom: "3vh" }}
        id="demo-radio-buttons-group-label"
      >
        Equathions
      </FormLabel>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="1"
        name="radio-buttons-group"
        value={value}
        onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
          setValue(event.target.value);
          setX(null);
          setY(null);
          setC(null);
        }}
      >
        <div className="flex radiolinear center_self">
          <FormControlLabel value="1" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`y'=y+(1+x)\cdot y^2`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="2" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`y'=y-x`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="3" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`y'=e^x-y`} />
            </Mafs>
          }
        </div>
      </RadioGroup>
    </FormControl>
  );
}

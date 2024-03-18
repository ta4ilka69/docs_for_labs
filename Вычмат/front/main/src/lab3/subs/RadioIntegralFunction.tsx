import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import { LaTeX, Mafs } from "mafs";

export default function RadioIntegralFunction({ value, setValue }) {
  return (
    <FormControl>
      <FormLabel
        sx={{ marginBottom: "3vh" }}
        id="demo-radio-buttons-group-label"
      >
        Integrals
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
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\int\limits_a^b (x-1)^2 dx`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="2" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\int\limits_a^b \dfrac{\sin{\pi x}}{2} dx`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="3" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX at={[0, 0]} tex={String.raw`\int\limits_a^b \dfrac{\sqrt{x}}{e^x-1}dx`} />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="4" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\int\limits_a^b \bigg(\cos{\pi x}-e^{\sin{\pi x}}+1\bigg) dx`}
              />
            </Mafs>
          }
        </div>
        <div className="flex radiolinear center_self">
          <FormControlLabel value="5" control={<Radio />} label="" />{" "}
          {
            <Mafs width={400} height={90} pan={false}>
              <LaTeX
                at={[0, 0]}
                tex={String.raw`\int\limits_a^b \frac{1}{(x-1)(x-3)} dx`}
              />
            </Mafs>
          }
        </div>
      </RadioGroup>
    </FormControl>
  );
}

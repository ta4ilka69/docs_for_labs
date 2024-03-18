import * as React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";

export default function RadioMethodsL({value, setValue}) {
  return (
    <FormControl>
      <FormLabel sx={{marginTop:"3vh", marginBottom:"3vh"}} id="demo-radio-buttons-group-label">Methods</FormLabel>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="1"
        name="radio-buttons-group"
        value={value}
        onChange={(event: React.ChangeEvent<HTMLInputElement>) => {setValue(event.target.value)}}
      >
        <div className = "flex radiolinear center_self">
        <FormControlLabel
          value="1"
          control={<Radio color="secondary"/>}
          label="Binary search"
        />
        </div>
        <div className = "flex radiolinear center_self">
        <FormControlLabel
          value="2"
          control={<Radio color="secondary"/>}
          label="Secant method"
        />
        </div>
        <div className = "flex radiolinear center_self">
        <FormControlLabel
          value="3"
          control={<Radio color="secondary"/>}
          label="Simple iteration method"/>
        </div>
      </RadioGroup>
    </FormControl>
  );
}

import React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
export default function InputDiff({ xn, ee, setXN, setE , x0, y0, setX0, setY0}) {
  let usersData = (
    <div className="inputColumn">
      <TextField
        required
        id="outlined-required"
        label="ε"
        value={ee}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setE(e.target.value)
        }
      />
      <TextField
        required
        id="outlined-required"
        label="x0"
        value={x0}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setX0(e.target.value)
        }
      />
      <TextField
        required
        id="outlined-required"
        label="y0"
        value={y0}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setY0(e.target.value)
        }
      />
      <TextField
        required
        id="outlined-required"
        label="xn"
        defaultValue={xn}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setXN(e.target.value)
        }
      />
    </div>
  );
  return (
    <Box
      component="form"
      sx={{
        "& .MuiTextField-root": { m: 1, width: "25ch" },
      }}
      noValidate
      autoComplete="off"
    >
      {usersData}
    </Box>
  );
}

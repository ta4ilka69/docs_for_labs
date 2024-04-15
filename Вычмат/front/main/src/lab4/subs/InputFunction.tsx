import React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
export default function InputFunction({f, setF, a, setA, b, setB}) {
  let usersData = (
    <div className="inputColumn">
      <TextField
        required
        id="outlined-required"
        label="f(x)"
        defaultValue={f}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setF(e.target.value)
        }
      />
      <TextField
        required
        id="outlined-required"
        label="a"
        defaultValue={a}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setA(e.target.value)
        }
      />
      <TextField
        required
        id="outlined-required"
        label="b"
        defaultValue={b}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setB(e.target.value)
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

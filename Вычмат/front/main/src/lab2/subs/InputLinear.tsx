import React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
export default function InputLinear({ a, b, ee, setA, setB, setE }) {
  let usersData = (
    <div className="inputColumn">
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
      <TextField
        required
        id="outlined-required"
        label="ε"
        value={ee}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setE(e.target.value)
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

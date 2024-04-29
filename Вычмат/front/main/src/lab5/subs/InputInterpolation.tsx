import React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
export default function InputInterpolation({
  m,
  setX,
  setY,
  setFile,
  setA,
  setB,
  setN,
  setXfind,
}) {
  let usersData = (
    <div className="inputColumn">
      {m == 1 && (
        <TextField
          required
          id="outlined-required"
          label="x"
          defaultValue={"0 1 2 3"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setX(e.target.value)
          }
        />
      )}
      {m == 1 && (
        <TextField
          required
          id="outlined-required"
          label="y"
          defaultValue={"0 1 4 9"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setY(e.target.value)
          }
        />
      )}
      {m == 1 && (
        <TextField
          required
          id="outlined-required"
          label="x*"
          defaultValue={"1"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setXfind(e.target.value)
          }
        />
      )}
      {m == 2 && (
        <TextField
          required
          id="outlined-required"
          label="filename"
          defaultValue={"file"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setFile(e.target.value)
          }
        />
      )}
      {(m == 3 || m == 4) && (
        <TextField
          required
          id="outlined-required"
          label="a"
          defaultValue={"0"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setA(e.target.value)
          }
        />
      )}
      {(m == 3 || m == 4) && (
        <TextField
          required
          id="outlined-required"
          label="b"
          defaultValue={"2"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setB(e.target.value)
          }
        />
      )}
      
      {(m == 3 || m == 4) && (
        <TextField
          required
          id="outlined-required"
          label="n"
          defaultValue={"10"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setN(e.target.value)
          }
        />
      )}
      {(m == 3 || m == 4) && (
        <TextField
          required
          id="outlined-required"
          label="x*"
          defaultValue={"1"}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setXfind(e.target.value)
          }
        />
      )}
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

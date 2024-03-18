import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import React from "react";
import Typography from "@mui/material/Typography";
import Toolbar from "@mui/material/Toolbar";

const Lab2 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography
        variant="h4"
        component="div"
        fontStyle={{ fontFamily: "Playpen Sans" }}
        marginBottom={2}
      >
        Lab 2
      </Typography>
      <Toolbar sx={{ justifyContent: "space-around",marginBottom:"3vh"}}>
        <Button variant="contained" href="/lab2/linear">
          {"Нелинейное уравнение"}
        </Button>
        <Button variant="contained" href="/lab2/system">
          {"Нелинейная система"}
        </Button>
      </Toolbar>
      <h3>Choose the variant</h3>
    </Box>
  );
};

export default Lab2;

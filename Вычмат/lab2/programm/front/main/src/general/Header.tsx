import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import React from "react";

export default function ButtonAppBar() {
  return (
    <Box sx={{ flexGrow: 1}}>
      <AppBar color="inherit" position="static">
        <Toolbar sx={{ justifyContent: "space-around" }}>
          <Typography variant="h6" component="div" className="fontik" fontStyle={{fontFamily: "Playpen Sans"}}>
            Artem Balin
          </Typography>
          <Button variant="outlined" href="/">
              {"Home"}
            </Button>
            <Button variant="outlined" href="/lab2">
              {"Lab 2"}
            </Button>
            <Button variant="outlined" href="/lab3">
              {"Lab 3"}
            </Button>
            <Button variant="outlined" href="/lab4">
              {"Lab 4"}
            </Button>
            <Button variant="outlined" href="/lab5">
              {"Lab 5"}
            </Button>
            <Button variant="outlined" href="/lab6">
              {"Lab 6"}
            </Button>
            <Typography variant="h6" component="div" className="fontik" fontStyle={{fontFamily: "Playpen Sans"}}>
            P3212
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

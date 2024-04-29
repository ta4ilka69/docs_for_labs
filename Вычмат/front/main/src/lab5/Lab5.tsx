import Box from "@mui/material/Box";
import React from "react";
import Typography from "@mui/material/Typography";
import Interpolation from "./Interpolation";

const Lab5 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography
        variant="h4"
        component="div"
        fontStyle={{ fontFamily: "Playpen Sans" }}
        marginBottom={2}
      >
        Lab 5
      </Typography>
      <Interpolation></Interpolation>
    </Box>
  );
};

export default Lab5;

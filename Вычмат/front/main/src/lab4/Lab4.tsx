import Box from "@mui/material/Box";
import React from "react";
import Typography from "@mui/material/Typography";
import Approximation from "./Approximation";

const Lab4 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography
        variant="h4"
        component="div"
        fontStyle={{ fontFamily: "Playpen Sans" }}
        marginBottom={2}
      >
        Lab 4
      </Typography>
      <Approximation/>
    </Box>
  );
};

export default Lab4;

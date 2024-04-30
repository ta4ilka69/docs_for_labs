import Box from "@mui/material/Box";
import React from "react";
import Typography from "@mui/material/Typography";
import Diffur from "./Diffur";


const Lab6 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography
        variant="h4"
        component="div"
        fontStyle={{ fontFamily: "Playpen Sans" }}
        marginBottom={2}
      >
        Lab 6
      </Typography>
      <Diffur />
    </Box>
  );
};

export default Lab6;

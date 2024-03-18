import Box from "@mui/material/Box";
import React from "react";
import Typography from "@mui/material/Typography";
import Integrals from "./Integrals";

const Lab3 = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography
        variant="h4"
        component="div"
        fontStyle={{ fontFamily: "Playpen Sans" }}
        marginBottom={2}
      >
        Lab 3
      </Typography>
      <Integrals></Integrals>
    </Box>
  );
};

export default Lab3;

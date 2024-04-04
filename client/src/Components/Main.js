import React from "react";
import backgroundImage from "../assets/package.webp";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const Main = () => {
  return (
    <div>
      <Box
      // sx={{
      //   p: 10,
      //   height: { sm: "120vh", md: "140vh", lg: "140vh", xl: "140vh" },

      //   backgroundSize: "cover",
      //   backgroundPosition: "center",
      // }}
      >
        <Container
          maxWidth="md"
          sx={{
            color: "#32004C",
          }}
        >
          <Typography
            variant="h5"
            align="center"
            sx={{
              padding: "20px",
              paddingBottom: "0px",
              fontWeight: "bold",
              fontSize: "30px",
            }}
            gutterBottom
          ></Typography>
          <Typography
            variant="subtitle1"
            align="center"
            sx={{
              padding: "20px",
              fontSize: "18px",
            }}
            paragraph
          ></Typography>
          <Button
            variant="contained"
            color="primary"
            sx={{ borderRadius: "999px" }}
          ></Button>
          <Typography
            component="div"
            align="center"
            sx={{
              maxWidth: "100%",
              height: "auto",
              padding: "20px",
              paddingTop: "80px",
            }}
          >
            <img
              src={backgroundImage}
              alt="backgroundImage "
              style={{ width: "100%" }}
            />
          </Typography>
        </Container>
      </Box>
    </div>
  );
};

export default Main;

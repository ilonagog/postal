import "./App.css";
import React from "react";
import Main from "./Components/Main";
import { Routes, Route } from "react-router-dom";
import Navigation from "./Components/Navigation";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import Signup from "./Components/Signup";

const theme = createTheme({
  palette: {
    primary: {
      main: "#7383b6",
    },
  },
});
function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Navigation />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </ThemeProvider>
    </div>
  );
}

export default App;

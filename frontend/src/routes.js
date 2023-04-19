import React from "react";
import { BrowserRouter as Router, Routes, Route,  } from "react-router-dom";
import Cadastro from "./pages/Cadastro";
import Home from "./pages/Home";
import Login from "./pages/Login";

function Rotas() {
  return (
    <Router>
      <Routes>
        <Route  path="/login" element={<Login/>} />
        <Route  path="/cadastro" element={<Cadastro/>} />
        <Route  path="/" element={<Home/>} />
      </Routes>
    </Router>
  );
}


export default Rotas;
import React, { useState } from "react";
import "./Login.css";
import "../../Global.css"
import Header from "../../Components/Header/Header.js"
import { useNavigate }  from "react-router-dom";

function Login() {
  const [email, setEmail]  = useState();
  const [Password, setPassword] = useState();
  const navigate = useNavigate();

  function login() {
    alert("Bem Vindo! ")
    navigate("/");
  }

  return (
    <div className="container">
      
      <Header />


      <section className="card-login">
        <div className="text_login">
          <p>
            Vamos começar?
            <br />
            Faça seu login logo abaixo
          </p>
        </div>

        <div className="form_container">

          <div className="form_itens">
            <form action="/criar-conta" method="post">

              <div className="input_form">
                <label for="email">
                  <p>Email:</p>
                </label>{" "}
                <br />
                <input
                  type="email"
                  id="email"
                  name="email"
                  placeholder="Digite seu endereço de email"
                  required
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <br />

              <div className="input_form">
                <label for="senha">
                  <p>Senha:</p>
                </label>{" "}
                <br />
                <input
                  type="password"
                  id="senha"
                  name="senha"
                  placeholder="Digite sua senha"
                  required
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>

              <br />

              <div className="submit_form">
                <input type="submit" value="Confirmar" onClick={login}/>
              </div>

            </form>
          </div>

          <div className="form_itens">
            <a href="/cadastro">
              Criar Conta
            </a>
          </div>

        </div>
        
      </section>
    </div>
  );
}

export default Login;

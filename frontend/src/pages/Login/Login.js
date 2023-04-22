import React from "react";
import "./Login.css";
import logo from "./Audio Wave.png"

function Login() {
  return (
    <div className="login_container">
      <div className="Logo">
        <img src={logo} ></img>
        <p>Speech Integrator</p>
      </div>
      <section className="user_card">
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
              <input type="email" id="email" name="email" placeholder = "Digite seu endereço de email" required />
            </div>
            <br />

            <div className="input_form">
              <label for="senha">
                <p>Senha:</p>
              </label>{" "}
              <br />
              <input type="password" id="senha" name="senha" placeholder = "Digite sua senha"  required />
            </div>
            <br />
            <div className="submit_form">
            <input type="submit" value="Confirmar" />
            </div>
          </form>
          </div>
          <div className="form_itens">
            <a href="https://www.google.com" target="_blank">
              Criar Conta
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Login;

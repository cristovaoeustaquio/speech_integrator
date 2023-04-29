import React, { useState } from "react";
import "./Cadastro.css";
import "../../Global.css";
import Header from "../../Components/Header/Header.js";
import { useNavigate } from "react-router-dom";

function Cadastro() {
  const [name, setName] = useState();
  const [email, setEmail] = useState();
  const [Password, setPassword] = useState();
  const [ConfPassword, setConfPassword] = useState();
  const navigate = useNavigate();

  function login() {
    alert("Bem Vindo! ");
    navigate("/");
  }

  return (
    <div className="container">
      <Header />
      <section className="card-create-user">
      /*
        <div className="subtitle">
          <p>
            Vamos começar?
          </p>
        </div>
        <div className="second-message">
          <p>
            Crie sua conta para utilizar nossos serviços com facilidade.
          </p>
        </div>
      
        <div className="form_container">
          <div className="form_itens">
            <form action="/criar-conta" method="post">
              <div className="input_form">
                <label for="nome">
                  <p>Nome:</p>
                </label>{" "}
                <br />
                <input
                  type="text"
                  id="nome"
                  name="nome"
                  placeholder="Digite seu o seu nome"
                  required
                  onChange={(e) => setName(e.target.value)}
                />
              </div>
              <div className="input_form">
                <label for="email">
                  <p>Email:</p>
                </label>{" "}
                <br />
                <input
                  type="text"
                  id="email"
                  name="email"
                  placeholder="Digite seu o seu endereço de email"
                  required
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div className="input_form">
                <label for="senha">
                  <p>Senha:</p>
                </label>{" "}
                <br />
                <input
                  type="password"
                  id="senha"
                  name="senha"
                  placeholder="Digite a sua senha"
                  required
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
              <div className="input_form">
                <label for="confsenha">
                  <p>Confirmar Senha:</p>
                </label>{" "}
                <br />
                <input
                  type="password"
                  id="confsenha"
                  name="confsenha"
                  placeholder="Confirme a sua senha"
                  required
                  onChange={(e) => setConfPassword(e.target.value)}
                />
              </div>              
              <br />
              <div className="submit_form">
                <input type="submit" value="Confirmar" onClick={login} />
              </div>
            </form>
          </div>
          <div className="form_itens">
            <a href="/login">Fazer Login</a>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Cadastro;

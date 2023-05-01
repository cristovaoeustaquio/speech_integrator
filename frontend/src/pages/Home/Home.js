import React, { useState } from "react";
import "./Home.css";
import "../../Global.css";
import Header from "../../Components/Header/Header.js";
import Messages from "../../Components/Messages/Messages.js";

import { useNavigate } from "react-router-dom";
import mic from "../../Images/Vector.png";

const dados = [
  { question: "Hello Chat GPT!", anwser: "Hello Human!" },
  { question: "Question 1", anwser: "Anwser 1" },
  { question: "Question 2", anwser: "Anwser 2" },
  { question: "Question 3", anwser: "Anwser 3" },
  { question: "Question 4", anwser: "Anwser 4"}
];

function Home() {
  return (
    <div className="container">
      <Header />
      <section className="home_card">
        <div className="home_header">
          <p>Olá, [Nome de Usuários], faça uma pergunta.</p>
          <div className="sair_button">Sair</div>
        </div>
        <div className="history">
          <div className="messages_content">
            {dados.map((linha, index) => (
              <tr key={index}>
                <Messages question={linha.question} anwser={linha.anwser} />
              </tr>
            ))}
          </div>
          <div className="talk_button">
            <div className="mic">
              <img src={mic}></img>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;

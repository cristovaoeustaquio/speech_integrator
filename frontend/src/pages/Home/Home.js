import React, { useState } from "react";
import "./Home.css";
import "../../Global.css";
import Header from "../../Components/Header/Header.js";
import Messages from "../../Components/Messages/Messages.js";

import { useNavigate } from "react-router-dom";
import mic from "../../Images/Vector.png";

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
          <Messages />  
          <Messages />
          <Messages />
          <Messages />
          <Messages />
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

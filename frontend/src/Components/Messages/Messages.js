import "./Messages.css";

import play from "../../Images/play.png";


export default function Messages() {
  return (
    <div className="messages">
    <div className="question_content">
      <div className="question">
      <img src={play}></img>
      </div>
    </div>
    <div className="anwser_content">
      <div className="anwser">
      <img src={play}></img>
      </div>
    </div>
  </div>
  );
}

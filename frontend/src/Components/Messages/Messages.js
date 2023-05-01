import "./Messages.css";
import { useState, useRef } from "react";
import play from "../../Images/play.png";
import audioQuestion from "../../Audios/recorded_audio2.wav";
import audioAwnser from "../../Audios/output.wav";

export default function Messages(props) {
  const [isPlayingQuestion, setIsPlayingQuestion] = useState(false);
  const [isPlayingAnwser, setIsPlayingAnwser] = useState(false);
  const audioRefQ = useRef(null);
  const audioRefA = useRef(null);

  function handleClickQuestion() {
    setIsPlayingQuestion(!isPlayingQuestion);
    if (!isPlayingQuestion) {
      audioRefQ.current.play();
    } else {
      audioRefQ.current.pause();
    }
  }

  function handleClickAnwser() {
    setIsPlayingAnwser(!isPlayingAnwser);
    if (!isPlayingAnwser) {
      audioRefA.current.play();
    } else {
      audioRefA.current.pause();
    }
  }

  return (
    <div className="messages">
      <div className="question_content">
        <div className="question">
          <div className="question_play">
            <img src={play} onClick={handleClickQuestion}></img>
            <audio ref={audioRefQ} src={audioQuestion} />
          </div>
          <div className="question_text">{props.question}</div>
        </div>
      </div>
      <div className="anwser_content">
        <div className="anwser">
          <div className="anwser_play">
            <img src={play} onClick={handleClickAnwser}></img>
            <audio ref={audioRefA} src={audioAwnser} />
          </div>
          <div className="anwser_text">{props.anwser}</div>
        </div>
      </div>
    </div>
  );
}

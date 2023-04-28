import logo from "../../Images/Audio Wave.png";
import "./Header.css";

export default function Header() {
  return (
    <div className="Logo">
      <img src={logo}></img>
      <p>Speech Integrator</p>
    </div>
  );
}

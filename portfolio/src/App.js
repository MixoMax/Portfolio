import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

import MainContent from './pages/main-content';

function App() {
  useEffect(() => {
    var clickables = document.querySelectorAll(".clickable");
    clickables.forEach((clickable) => {
      var href = clickable.getAttribute("href");
      clickable.addEventListener("click", () => {
        window.location.href = href;
      })
      console.log(href);
    });
  }, []);



  return (
    <div className="App vbox">
      <MainContent />
      <div id="middle_line" style={{height: "100vh", width: "2px", backgroundColor: "black", position: "absolute", left: "50%", top: "0"}}></div>
      <div id="middle_line" style={{height: "2px", width: "100vw", backgroundColor: "black", position: "absolute", left: "0", top: "50%"}}></div>
    </div>
  );
}

export default App;

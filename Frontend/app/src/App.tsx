import React from 'react';
import { useState, useEffect } from "react";
import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/time`).then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <p>The current time is {currentTime}.</p>
    </div>
  );
}


export default App;

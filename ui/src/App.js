import React, { useState, useEffect } from "react";
import SocketClient from "socket.io-client"; 

const ENDPOINT = "http://127.0.0.1:5000";
const socket = SocketClient.connect(ENDPOINT); 

function App() {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");

  const getMessages = () => {
    socket.on("message", msg => {
      setMessages([...messages, msg])
    });
  };

  useEffect(() => {
    socket.on("connect", (data) => console.log(data));
  }, []);

  return (
    <div>
      {messages.length > 0 && messages.map(msg => (
        <p>{msg}</p>
      ))}
    </div>
  );
}

export default App;
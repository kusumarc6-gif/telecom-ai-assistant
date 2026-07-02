import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! 👋 Welcome to Enterprise AI Telecom Assistant. How can I help you today?",
    },
  ]);

  const sendMessage = async () => {
    if (!question.trim()) return;

    const userMessage = {
      sender: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        question: question,
      });

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: res.data.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Unable to connect to the AI server.",
        },
      ]);
    }

    setQuestion("");
  };

  return (
    <div className="app">
      <div className="header">
        <h1>📡 Enterprise AI Telecom Assistant</h1>
        <p>AI Powered Customer Support System</p>
      </div>

      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={question}
          placeholder="Ask your telecom question..."
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
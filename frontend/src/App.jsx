import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const [summary, setSummary] = useState("");
  const [quiz, setQuiz] = useState("");

  const [loading, setLoading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState("");

  // Upload PDF
  const uploadPDF = async () => {
    if (!file) {
      alert("Please choose a PDF.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setUploadStatus("✅ PDF uploaded successfully!");
      alert(res.data.message);
    } catch (err) {
      console.error(err);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  // Ask Question
  const askQuestion = async () => {
    if (!question) {
      alert("Please enter a question.");
      return;
    }

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question,
        }
      );

      setAnswer(res.data.answer);
    } catch (err) {
      console.error(err);
      alert("Question failed.");
    } finally {
      setLoading(false);
    }
  };

  // Summary
  const generateSummary = async () => {
    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/summary"
      );

      setSummary(res.data.summary);
    } catch (err) {
      console.error(err);
      alert("Summary failed.");
    } finally {
      setLoading(false);
    }
  };

  // Quiz
  const generateQuiz = async () => {
    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/quiz"
      );

      setQuiz(res.data.quiz);
    } catch (err) {
      console.error(err);
      alert("Quiz failed.");
    } finally {
      setLoading(false);
    }
  };

  // Clear
  const clearResults = () => {
    setQuestion("");
    setAnswer("");
    setSummary("");
    setQuiz("");
    setUploadStatus("");
  };

  return (
    <div className="container">
      <h1>📘 StudyPilot AI</h1>

      <p
        style={{
          textAlign: "center",
          color: "#94a3b8",
          marginBottom: "30px",
        }}
      >
        Your AI-Powered Learning Companion
      </p>

      {loading && (
        <h3 style={{ textAlign: "center" }}>
          🤖 AI is processing...
        </h3>
      )}

      {/* Upload */}

      <div className="card">
        <h2>📄 Upload PDF</h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br />
        <br />

        <button onClick={uploadPDF}>
          Upload PDF
        </button>

        {uploadStatus && (
          <p
            style={{
              color: "lightgreen",
              marginTop: "15px",
            }}
          >
            {uploadStatus}
          </p>
        )}
      </div>

      {/* Chat */}

      <div className="card">
        <h2>💬 Ask AI</h2>

        <input
          className="question-box"
          type="text"
          placeholder="Ask a question from your notes..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <br />
        <br />

        <button onClick={askQuestion}>
          Ask AI
        </button>

        <div className="markdown">
          <ReactMarkdown>{answer}</ReactMarkdown>
        </div>
      </div>

      {/* Summary */}

      <div className="card">
        <h2>📝 Summary</h2>

        <button onClick={generateSummary}>
          Generate Summary
        </button>

        <div className="markdown">
          <ReactMarkdown>{summary}</ReactMarkdown>
        </div>
      </div>

      {/* Quiz */}

      <div className="card">
        <h2>🎯 Quiz</h2>

        <button onClick={generateQuiz}>
          Generate Quiz
        </button>

        <div className="markdown">
          <ReactMarkdown>{quiz}</ReactMarkdown>
        </div>
      </div>

      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <button onClick={clearResults}>
          Clear Results
        </button>
      </div>

      <hr />

      <p
        style={{
          textAlign: "center",
          color: "gray",
          marginTop: "30px",
        }}
      >
        Built with ❤️ using React, FastAPI, ChromaDB & Groq
      </p>
    </div>
  );
}

export default App;
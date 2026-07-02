# 📡 Enterprise AI Telecom Assistant

An AI-powered Telecom Assistant built using FastAPI, React, LangChain, FAISS, Hugging Face Embeddings, and Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- AI-powered telecom chatbot
- RAG-based document retrieval
- FastAPI backend
- React frontend
- FAISS Vector Database
- Hugging Face Embeddings
- Telecom datasets support
- REST API
- Interactive web interface

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers

### Frontend
- React
- Vite
- Axios

### Database
- CSV Datasets
- FAISS Vector Store

---

## 📂 Project Structure

```
telecom-ai-assistant
│
├── backend
│   ├── app
│   ├── data
│   ├── chroma_db
│   ├── faiss_index
│   ├── notebooks
│   ├── .env
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── datasets
├── database
├── documents
├── screenshots
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository_url>
cd telecom-ai-assistant
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file

```
GOOGLE_API_KEY=your_api_key
```

Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

## 💬 Sample Questions

- What telecom plans are available?
- Show broadband plans.
- What is Premium 799?
- Explain Fiber 499 plan.
- What are recharge options?

---

## 📸 Screenshots

Store screenshots inside

```
screenshots/
```

Example:

- Home Page
- Chat Interface
- Swagger API
- Backend Running

---

## Future Improvements

- Voice Assistant
- Authentication
- Chat History
- Admin Dashboard
- Deployment on AWS
- Streaming Responses

---

## Author

**Kusuma R C**

AI Engineer | Machine Learning | Generative AI | RAG | FastAPI | React
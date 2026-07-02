# 📡 Enterprise AI Telecom Assistant

An AI-powered Telecom Assistant built using **React, FastAPI, LangChain, FAISS, Hugging Face Embeddings, and Groq Llama 3.3 70B**.

The application enables telecom employees to retrieve customer information instantly and answer telecom-related questions using a hybrid approach that combines **Structured Search** and **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Project Overview

Searching through multiple telecom records manually is time-consuming.

This project solves that problem by allowing users to ask questions in natural language.

Examples:

- Show details of customer CUST00001
- Show billing history for customer CUST00001
- Show recharge history for customer CUST00001
- Show complaints for customer CUST00001
- What telecom plans are available?
- How do I activate a new SIM?

The assistant intelligently decides whether to:

- Perform **Structured Search** for customer records
- Use **RAG** for telecom knowledge-based questions

---

# 🏗 Architecture

```
                   User
                     │
                     ▼
             React Frontend
                     │
               REST API Request
                     │
                     ▼
              FastAPI Backend
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
 Structured Search            RAG Pipeline
     (Pandas)                 (LangChain)
      │                             │
      ▼                             ▼
 CSV Datasets              FAISS Vector Store
                                    │
                                    ▼
                    HuggingFace Embeddings
                     (all-MiniLM-L6-v2)
                                    │
                                    ▼
                      Groq Llama 3.3 70B
                                    │
                                    ▼
                            Final Response
```

---

# ✨ Features

- Customer Search
- Billing History Search
- Recharge History Search
- Complaint Search
- Service Request Search
- Customer Feedback Search
- Telecom Knowledge Assistant
- Natural Language Queries
- Retrieval-Augmented Generation (RAG)
- Semantic Similarity Search
- FastAPI REST APIs
- Modern React Chat Interface

---

# 🧠 RAG Pipeline

The project uses Retrieval-Augmented Generation (RAG) for answering telecom knowledge questions.

### Workflow

1. Load documents from:
   - CSV
   - TXT
   - JSON

2. Split documents using

```
RecursiveCharacterTextSplitter
```

3. Generate embeddings using

```
all-MiniLM-L6-v2
```

4. Store embeddings in

```
FAISS Vector Database
```

5. Convert the user's question into an embedding.

6. Perform Semantic Similarity Search.

7. Retrieve Top **3** relevant chunks (**k = 3**).

8. Pass retrieved context to

```
Groq Llama 3.3 70B
```

9. Generate the final response.

---

# 🔍 Similarity Search

This project uses **Vector Similarity Search** through FAISS.

The embedding of the user's query is compared with stored document embeddings.

The **Top 3 most semantically similar chunks** are retrieved before generating the answer.

---

# 📂 Supported Documents

- CSV
- TXT
- JSON

---

# 🛠 Tech Stack

### Frontend

- React.js
- Axios
- CSS

### Backend

- FastAPI
- Python

### AI & NLP

- LangChain
- Hugging Face Embeddings
- FAISS
- Groq Llama 3.3 70B
- RetrievalQA

### Data Processing

- Pandas

---

# 📁 Project Structure

```
telecom-ai-assistant
│
├── backend
│   ├── app
│   ├── data
│   ├── rag
│   └── search
│
├── frontend
│
├── documents
│   ├── csv
│   ├── json
│   └── txt
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/kusumarc6-gif/telecom-ai-assistant.git
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

Run

```bash
python app/rag/index_documents.py
```

Start Backend

```bash
uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 💬 Sample Questions

### Structured Search

```
Show details of customer CUST00001

Show billing history for customer CUST00001

Show recharge history for customer CUST00001

Show complaints for customer CUST00001

Show customer feedback for customer CUST00001
```

### RAG

```
What telecom plans are available?

Explain Fiber 799 Plan.

How do I activate a new SIM?

How can I troubleshoot slow internet?

How do I raise a complaint?

How can I contact customer support?
```

---

# 📈 Future Enhancements

- User Authentication
- Chat History
- Voice Assistant
- Live Database Integration
- Cloud Deployment
- AWS Integration
- Role-Based Access
- Dashboard & Analytics
- Multilingual Support

---

# 👨‍💻 Author

**Kusuma R C**

MCA Student | Aspiring AI Engineer & Data Analyst

Generative AI | NLP | LLM | RAG | Python | SQL | Power BI

---

## ⭐ If you like this project, don't forget to Star the repository!

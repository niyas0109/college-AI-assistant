# 🎓 AI College Assistant

An AI-powered college document assistant that uses **Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG)** to answer questions from college and university PDF documents.

## 🚀 Features

* 📄 Upload and process PDF documents
* 🔎 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Gemini-powered question answering
* 💬 Conversational chat interface
* 📚 Source and page references
* 🗂️ Support for multiple PDF documents
* 🛡️ Answers grounded in the provided documents

## 🏗️ How It Works

```text
College / University PDFs
          ↓
     PDF Extraction
          ↓
      Text Chunking
          ↓
   Sentence Transformers
          ↓
      FAISS Vector DB
          ↓
     Similarity Search
          ↓
   Relevant Document Chunks
          ↓
        Gemini LLM
          ↓
      AI Answer + Sources
```

## 🛠️ Technologies Used

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| Python                | Application development |
| Streamlit             | Web interface           |
| LangChain             | RAG pipeline            |
| Gemini                | Large Language Model    |
| FAISS                 | Vector database         |
| Sentence Transformers | Text embeddings         |
| PyMuPDF               | PDF document processing |

## 📁 Project Structure

```text
college-AI-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_database.py
│   ├── rag_pipeline.py
│   └── llm.py
│
└── data/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/niyas0109/college-AI-assistant.git
cd college-AI-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure Gemini API

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

**Never upload `.env` or your API key to GitHub.**

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Questions

You can ask questions such as:

* What is the minimum attendance requirement?
* What happens if attendance is below 75%?
* What are the examination regulations?
* Explain this regulation.
* Which page contains this information?

## 🎯 Project Objective

The goal of this project is to provide students with a simple AI-powered interface for accessing information from large college and university documents without manually searching through lengthy PDF files.

## 🔍 RAG Approach

The system uses Retrieval-Augmented Generation instead of relying only on the language model's general knowledge.

The application:

1. Loads PDF documents.
2. Extracts their text.
3. Splits the text into smaller chunks.
4. Converts chunks into vector embeddings.
5. Stores the embeddings in FAISS.
6. Retrieves relevant chunks for a question.
7. Sends the retrieved context to Gemini.
8. Generates an answer based on the provided documents.
9. Displays the relevant source information.

## 🔐 Security

API keys and other sensitive configuration files should never be committed to GitHub.

The `.gitignore` file excludes:

```text
.env
venv/
__pycache__/
vectorstore/
```

## 🚀 Future Improvements

* PDF-specific document selection
* Advanced document management
* Improved source citations
* PDF summarization
* Automatic FAQ generation
* User authentication
* Cloud deployment
* Conversation history
* Admin dashboard

## 👨‍💻 Author

**Niyas Ahmed**

B.Tech Artificial Intelligence and Data Science

## ⭐ Project

If you find this project useful, consider giving the repository a star on GitHub.

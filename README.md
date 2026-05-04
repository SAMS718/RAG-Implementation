# 🧠 RAG Pipeline (LangChain + Chroma + HuggingFace) — Ingestion + Retrieval

This project demonstrates a **complete Retrieval pipeline** of a RAG system using LangChain. It includes:

* 📥 Document ingestion
* ✂️ Chunking
* 🧠 Embedding generation (HuggingFace - free)
* 🗄️ Vector storage using ChromaDB
* 🔍 Semantic retrieval (NO LLM used)

---

## 🚀 Features

* Load `.txt` files from a directory
* Split documents into chunks
* Generate embeddings locally (no API cost)
* Store vectors in ChromaDB
* Retrieve top-k relevant documents using semantic search
* Fully offline after initial model download

---

## 🏗️ Architecture

```id="arch123"
Ingestion Phase:
Documents → Loader → Text Splitter → Embeddings → ChromaDB

Retrieval Phase:
Query → Embedding → Similarity Search → Top-K Documents
```

---

## 📁 Project Structure

```id="struct456"
RAG_Code/
│
├── docs/                  # Input documents (.txt)
├── db/
│   └── chroma_db/         # Persisted vector store
├── ingestion_pipeline.py  # Creates vector DB
├── retrieval_pipeline.py  # Retrieves relevant documents
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repo

```bash id="cmd1"
git clone https://github.com/your-username/rag-pipeline.git
cd rag-pipeline
```

### 2️⃣ Create virtual environment

```bash id="cmd2"
python -m venv venv
```

### Activate:

* Windows:

```bash id="cmd3"
venv\Scripts\activate
```

* Mac/Linux:

```bash id="cmd4"
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash id="cmd5"
pip install langchain langchain-community langchain-chroma langchain-text-splitters sentence-transformers python-dotenv
```

---

## 📄 Usage

### 🧩 Step 1: Add Documents

Place `.txt` files inside:

```id="cmd6"
docs/
```

---

### ⚙️ Step 2: Run Ingestion Pipeline

```bash id="cmd7"
python ingestion_pipeline.py
```

✔️ This will:

* Load documents
* Split into chunks
* Generate embeddings
* Store them in ChromaDB

---

### 🔍 Step 3: Run Retrieval Pipeline

```bash id="cmd8"
python retrieval_pipeline.py
```

✔️ This will:

* Convert query into embedding
* Perform similarity search
* Return top-k relevant chunks

---

## 🧠 Embedding Model

Using:

```id="cmd9"
all-MiniLM-L6-v2
```

* Lightweight (~100MB)
* Fast and efficient
* Works offline
* Ideal for semantic search

---

## 🔍 Sample Query

```id="cmd10"
query = "which island does SpaceX lease for its launches in the Pacific?"
```

### Output:

```id="cmd11"
User Query: which island does SpaceX lease...

--- Context ---
Document 1:
[Relevant chunk]

Document 2:
[Relevant chunk]
```

---

## ⚠️ Important Notes

* ❌ No LLM is used in retrieval phase
* ✅ Results are purely based on **vector similarity (cosine)**
* ⚡ ChromaDB automatically handles similarity metric
* 📌 Ensure same embedding model is used in ingestion & retrieval

---

## 🔥 Key Learnings

* Difference between **Ingestion vs Retrieval phase**
* Importance of **consistent embeddings**
* How vector databases perform semantic search
* Building blocks of a full RAG system

---

## 🚀 Future Improvements

* Add LLM for answer generation (full RAG)
* Build API (FastAPI)
* Add UI (Streamlit / React)
* Support PDFs, HTML, and other formats
* Implement hybrid search (keyword + vector)

---

## 🏷️ Tags

```id="cmd12"
#RAG #LangChain #ChromaDB #HuggingFace #NLP #VectorSearch #AIProjects
```

---

## 📜 License

MIT License

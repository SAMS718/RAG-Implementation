# 🧠 Conversational RAG Pipeline (LangChain + Chroma + HuggingFace) — Fully Offline

This project implements a **complete conversational Retrieval-Augmented Generation (RAG) system** using LangChain, ChromaDB, and HuggingFace models.

Unlike basic RAG pipelines, this system supports:

* 🔁 **Conversation history**
* 🔍 **Context-aware query rewriting**
* 🤖 **Answer generation using local LLM (FLAN-T5)**
* ⚡ **Fully offline execution (no OpenAI API required)**

---

## 🚀 Features

* 📂 Load `.txt` documents from a directory
* ✂️ Split documents into chunks
* 🧠 Generate embeddings using HuggingFace (offline)
* 🗄️ Store vectors in ChromaDB
* 🔍 Retrieve relevant documents using semantic search
* 💬 Maintain **conversation history**
* 🔄 Rewrite queries based on previous context
* 🤖 Generate answers using FLAN-T5 (`model.generate`)
* ⚡ Works fully offline after model download

---

## 🏗️ Architecture

```id="arch003"
Ingestion Phase:
Documents → Loader → Text Splitter → Embeddings → ChromaDB

Retrieval Phase:
User Query → Context-Aware Rewrite → Embedding → Similarity Search

Generation Phase:
Conversation History + Context + Query → FLAN-T5 → Final Answer
```

---

## 📁 Project Structure

```id="struct003"
RAG_Code/
│
├── docs/                  # Input documents (.txt)
├── db/
│   └── chroma_db/         # Vector database
├── ingestion_pipeline.py  # Builds vector store
├── retrieval_pipeline.py  # Conversational RAG system
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash id="cmd41"
git clone https://github.com/your-username/conversational-rag.git
cd conversational-rag
```

---

### 2️⃣ Create Virtual Environment

```bash id="cmd42"
python -m venv venv
```

Activate:

* Windows:

```bash id="cmd43"
venv\Scripts\activate
```

* Mac/Linux:

```bash id="cmd44"
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="cmd45"
pip install langchain langchain-community langchain-chroma langchain-text-splitters sentence-transformers transformers torch python-dotenv
```

---

## 📄 Usage

### 🧩 Step 1: Add Documents

Place `.txt` files inside:

```id="cmd46"
docs/
```

---

### ⚙️ Step 2: Run Ingestion Pipeline

```bash id="cmd47"
python ingestion_pipeline.py
```

---

### 💬 Step 3: Start Chat

```bash id="cmd48"
python retrieval_pipeline.py
```

---

## 💬 Example Interaction

```id="cmd49"
Ask me questions! Type 'quit' to exit.

Your question: Where is SpaceX headquartered?

Answer: SpaceX is headquartered at Starbase near Brownsville, Texas.

Your question: Where was it located before?

Answer: It was previously headquartered in Hawthorne, California.
```

---

## 🧠 Models Used

### 🔹 Embeddings

```id="cmd50"
all-MiniLM-L6-v2
```

* Lightweight (~100MB)
* Fast semantic similarity
* Fully local

---

### 🔹 LLM (Answer Generation)

```id="cmd51"
google/flan-t5-base
```

* Instruction-tuned
* Suitable for Q&A
* Runs offline

---

## 🔥 Key Implementation Details

### 🧠 Conversation Memory

* Maintains previous user and AI interactions
* Injected into prompt as text
* Enables context-aware responses

---

### 🔄 Query Rewriting

* Converts follow-up questions into standalone queries
* Improves retrieval accuracy

---

### ⚙️ Direct Model Inference

Instead of:

```python id="cmd52"
pipeline(...)
```

We use:

```python id="cmd53"
model.generate(...)
```

### ✅ Benefits:

* Avoids transformer version issues
* More stable execution
* Better control over outputs

---

## ⚠️ Limitations

* ❌ No advanced reasoning like GPT-4
* ⚠️ Depends heavily on retrieved documents
* ⚠️ Limited conversation memory quality
* 📦 Initial model download required

---

## 🔥 Key Learnings

* Building **end-to-end conversational RAG systems**
* Handling **context-aware retrieval**
* Managing **LLM limitations in offline setups**
* Designing **prompt-based memory systems**
* Avoiding dependency on paid APIs

---

## 🚀 Future Improvements

* Add reranking for better retrieval
* Integrate OpenAI / Claude (hybrid system)
* Build UI (Streamlit / React chat interface)
* Add support for PDFs & structured data
* Implement memory optimization

---

## 🏷️ Tags

```id="cmd54"
#RAG #ConversationalAI #LangChain #ChromaDB #HuggingFace #Transformers #NLP #AIProjects
```

---

## 📜 License

MIT License

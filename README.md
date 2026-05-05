# 🧠 Conversational RAG Pipeline (LangChain + Chroma + HuggingFace) — Fully Offline

This project implements a **complete conversational Retrieval-Augmented Generation (RAG) system** using LangChain, ChromaDB, and HuggingFace models.

It includes:

* 🔍 Semantic retrieval
* 💬 Conversation history
* 🔄 Query rewriting
* 🤖 Local LLM (FLAN-T5)
* ⚡ Fully offline execution

---

## 🚀 Features

* 📂 Load `.txt` documents
* ✂️ Advanced text chunking (Recursive splitting)
* 🧠 HuggingFace embeddings
* 🗄️ ChromaDB vector storage
* 🔍 Semantic search
* 💬 Conversational memory
* 🤖 Offline answer generation

---

## 🏗️ Architecture

```id="arch004"
Ingestion:
Documents → Recursive Text Splitter → Embeddings → ChromaDB

Retrieval:
Query → Context-Aware Rewrite → Embedding → Similarity Search

Generation:
History + Context + Query → FLAN-T5 → Answer
```

---

## ⚙️ Installation

```bash id="cmd61"
pip install langchain langchain-community langchain-chroma langchain-text-splitters sentence-transformers transformers torch python-dotenv
```

---

## ⚠️ Important Update (LangChain Modular Changes)

Recent versions of LangChain have split components into separate packages.

### ❌ Old Import (deprecated)

```python id="cmd62"
from langchain.text_splitter import CharacterTextSplitter
```

### ✅ New Import (correct)

```python id="cmd63"
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
```

---

## ✂️ Text Splitting Strategy

This project uses:

```id="cmd64"
RecursiveCharacterTextSplitter
```

### Why?

* Handles large paragraphs better
* Uses multiple separators (`\n\n`, `\n`, `.`, space)
* Produces cleaner semantic chunks
* Improves retrieval accuracy

---

## 💬 Conversational Flow

```id="cmd65"
User Query
   ↓
Rewrite Query (based on history)
   ↓
Retrieve Documents
   ↓
Combine Context + History
   ↓
FLAN-T5 (generate answer)
```

---

## 🧠 Models Used

### Embeddings

```id="cmd66"
all-MiniLM-L6-v2
```

### LLM

```id="cmd67"
google/flan-t5-base
```

---

## ⚙️ Key Design Choices

### ✅ Recursive Text Splitting

Improves chunk quality → better retrieval

### ✅ Direct Model Inference

```python id="cmd68"
model.generate()
```

Avoids pipeline version issues

### ✅ Text-Based Memory

Simple and efficient conversational history handling

---

## ⚠️ Notes

* LangChain APIs change frequently → modular imports required
* First run downloads models (~200MB)
* Retrieval quality directly affects answer quality

---

## 🚀 Future Improvements

* Hybrid search (keyword + vector)
* Reranking models
* UI (Streamlit chat app)
* Multi-document formats (PDF, HTML)

---

## 🏷️ Tags

```id="cmd69"
#RAG #LangChain #ChromaDB #HuggingFace #Transformers #ConversationalAI
```

---

## 📜 License

MIT License

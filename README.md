# 🧠 RAG Pipeline (LangChain + Chroma + HuggingFace) — Fully Offline

This project implements a **complete Retrieval-Augmented Generation (RAG) pipeline** using LangChain, ChromaDB, and HuggingFace models.

Unlike typical implementations, this project uses **direct transformer model inference (`model.generate`) instead of pipeline APIs**, ensuring better compatibility and stability across different environments.

---

## 🚀 Features

* 📂 Load `.txt` documents from a directory
* ✂️ Split documents into chunks
* 🧠 Generate embeddings using HuggingFace (offline & free)
* 🗄️ Store embeddings in Chroma vector database
* 🔍 Retrieve top-k relevant chunks using semantic search
* 🤖 Generate answers using FLAN-T5 (no API required)
* ⚡ Fully offline after initial model download

---

## 🏗️ Architecture

```id="arch002"
Ingestion Phase:
Documents → Loader → Text Splitter → Embeddings → ChromaDB

Retrieval Phase:
Query → Embedding → Similarity Search → Top-K Documents

Generation Phase:
Context + Query → FLAN-T5 (model.generate) → Final Answer
```

---

## 📁 Project Structure

```id="struct002"
RAG_Code/
│
├── docs/                  # Input documents (.txt)
├── db/
│   └── chroma_db/         # Persisted vector database
├── ingestion_pipeline.py  # Creates vector DB
├── retrieval_pipeline.py  # Retrieval + generation
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash id="cmd21"
git clone https://github.com/your-username/rag-pipeline.git
cd rag-pipeline
```

---

### 2️⃣ Create Virtual Environment

```bash id="cmd22"
python -m venv venv
```

Activate:

* Windows:

```bash id="cmd23"
venv\Scripts\activate
```

* Mac/Linux:

```bash id="cmd24"
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="cmd25"
pip install langchain langchain-community langchain-chroma langchain-text-splitters sentence-transformers transformers torch python-dotenv
```

---

## 📄 Usage

### 🧩 Step 1: Add Documents

Place `.txt` files inside:

```id="cmd26"
docs/
```

---

### ⚙️ Step 2: Run Ingestion Pipeline

```bash id="cmd27"
python ingestion_pipeline.py
```

✔️ Creates vector embeddings and stores them in ChromaDB

---

### 🔍 Step 3: Run Retrieval + Generation Pipeline

```bash id="cmd28"
python retrieval_pipeline.py
```

✔️ Retrieves relevant chunks and generates an answer

---

## 🧠 Models Used

### 🔹 Embeddings

```id="cmd29"
all-MiniLM-L6-v2
```

* Lightweight and fast
* Runs locally
* Optimized for semantic similarity

---

### 🔹 LLM (Answer Generation)

```id="cmd30"
google/flan-t5-base
```

* Instruction-tuned model
* Good for question answering
* Works fully offline

---

## ⚠️ Important Design Decision

Instead of using:

```python id="cmd31"
pipeline("text2text-generation")
```

This project uses:

```python id="cmd32"
model.generate()
```

### ✅ Why?

* Avoids **transformers version conflicts**
* More stable across environments
* Gives **better control over generation**
* Industry-relevant approach

---

## 🔍 Sample Query

```id="cmd33"
query = "Where is SpaceX headquartered?"
```

---

## 🧪 Sample Output

```id="cmd34"
User Query: Where is SpaceX headquartered?

--- Generated Response ---
SpaceX is headquartered at Starbase near Brownsville, Texas.
```

---

## ⚠️ Notes

* ❌ No OpenAI / paid API required
* ⚠️ Answer depends on retrieved context
* 📌 If context lacks answer → model may fail or respond minimally
* 📦 First run downloads models (~200–300MB)

---

## 🔥 Key Learnings

* Difference between **retrieval vs generation**
* Importance of **embedding consistency**
* Limitations of RAG when context is missing
* Handling **transformer compatibility issues**
* Using **direct model inference instead of pipelines**

---

## 🚀 Future Improvements

* Add reranking (improve retrieval accuracy)
* Integrate LLM APIs (OpenAI / Claude)
* Build UI (Streamlit / React)
* Add support for PDFs and structured data
* Implement conversational memory

---

## 🏷️ Tags

```id="cmd35"
#RAG #LangChain #ChromaDB #HuggingFace #Transformers #NLP #AIProjects
```

---

## 📜 License

MIT License

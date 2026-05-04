# NO LLM API (FREE VERSION) → Using HuggingFace instead of OpenAI

import os

# Chroma DB for vector storage and retrieval
from langchain_chroma import Chroma

# HuggingFace embeddings (same model used in ingestion pipeline)
from langchain_community.embeddings import HuggingFaceEmbeddings

# HuggingFace LLM pipeline
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Loading environment variables (good practice, even if not used here)
from dotenv import load_dotenv
load_dotenv()


# -----------------------------
# Step 1: Load Existing Vector DB
# -----------------------------
persistent_directory = "db/chroma_db"

# IMPORTANT: Same embedding model must be used as ingestion phase
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load ChromaDB (No chunks needed here → already stored)
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model
)


# -----------------------------
# Step 2: Define User Query
# -----------------------------
query = "which island does SpaceX lease for its launches in the Pacific?"

# Retriever fetches top-k relevant chunks using cosine similarity (default)
retriever = db.as_retriever(search_kwargs={"k": 5})  # Top 5 results retrieved

# Invoke retriever with query → returns relevant document chunks
relevant_docs = retriever.invoke(query)


# -----------------------------
# Step 3: Combine Retrieved Context
# -----------------------------
# Combine all retrieved chunks into a single context string
context = "\n\n".join([doc.page_content for doc in relevant_docs])

# Prompt template → guides the LLM behavior (simplified for better results)
combined_input = f"""
Context:
{context}

Question: {query}

Answer briefly:
"""


# -----------------------------
# Step 4: HuggingFace LLM (DIRECT MODEL CALL - FIXED)
# -----------------------------
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Function to generate answer manually (no pipeline issues)
def generate_answer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.3
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# -----------------------------
# Step 5: Generate Final Answer
# -----------------------------
response = generate_answer(combined_input)

print("\nUser Query:")
print(query)

print("\n--- Retrieved Context ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"\nDocument {i}:\n{doc.page_content}")

print("\n--- Generated Response ---")
print(response)

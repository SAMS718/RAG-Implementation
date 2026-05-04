# FULLY OFFLINE CHAT RAG (HuggingFace Version)

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv()


# -----------------------------
# Step 1: Load Vector DB
# -----------------------------
persistent_directory = "db/chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model
)


# -----------------------------
# Step 2: Load LLM (FLAN-T5)
# -----------------------------
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


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
# Step 3: Chat History (TEXT BASED)
# -----------------------------
chat_history = []


def ask_question(user_question):
    print(f"\n--- You asked: {user_question} ---")

    # -----------------------------
    # Step 1: Rewrite question (context-aware)
    # -----------------------------
    if chat_history:
        history_text = "\n".join(chat_history[-4:])  # last few turns

        rewrite_prompt = f"""
Given the conversation history:

{history_text}

Rewrite this question to be standalone:
{user_question}
"""

        search_question = generate_answer(rewrite_prompt)
        print(f"Searching for: {search_question}")

    else:
        search_question = user_question

    # -----------------------------
    # Step 2: Retrieve docs
    # -----------------------------
    retriever = db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(search_question)

    print(f"Found {len(docs)} relevant documents:")

    for i, doc in enumerate(docs, 1):
        preview = "\n".join(doc.page_content.split("\n")[:2])
        print(f"  Doc {i}: {preview}...")

    # -----------------------------
    # Step 3: Build prompt
    # -----------------------------
    context = "\n\n".join([doc.page_content for doc in docs])
    history_text = "\n".join(chat_history[-4:])

    combined_prompt = f"""
Conversation History:
{history_text}

Context:
{context}

Question: {user_question}

Answer clearly:
"""

    # -----------------------------
    # Step 4: Generate answer
    # -----------------------------
    answer = generate_answer(combined_prompt)

    # -----------------------------
    # Step 5: Store history
    # -----------------------------
    chat_history.append(f"User: {user_question}")
    chat_history.append(f"AI: {answer}")

    print(f"Answer: {answer}")
    return answer


# -----------------------------
# Step 6: Chat Loop
# -----------------------------
def start_chat():
    print("Ask me questions! Type 'quit' to exit.")

    while True:
        question = input("\nYour question: ")

        if question.lower() == "quit":
            print("Goodbye!")
            break

        ask_question(question)


if __name__ == "__main__":
    start_chat()
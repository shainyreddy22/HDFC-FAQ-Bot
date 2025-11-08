import gradio as gr
import requests
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import os
# 🔐 Your OpenRouter API key
API_KEY =  os.getenv("OPENROUTER_API_KEY", "").strip()

# Load FAISS index
index = faiss.read_index("faq_index.faiss")

# Load FAQ Q&A pairs
with open("faq_data.pkl", "rb") as f:
    faq_data = pickle.load(f)
questions = faq_data["questions"]
answers = faq_data["answers"]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Search in vector DB
def search_faq(query, top_k=1):
    query_embedding = model.encode([query]).astype('float32')
    distances, indices = index.search(query_embedding, top_k)
    top_idx = indices[0][0]
    return questions[top_idx], answers[top_idx]

# DeepSeek rephrasing
def rephrase_with_deepseek(user_question, matched_answer):
    prompt = f"""
You are a helpful customer support assistant for HDFC Bank.

The user asked: "{user_question}"

Here is the answer from the FAQ:
"{matched_answer}"

Please rephrase it in a polite, conversational tone. Make it more natural, helpful, and user-friendly.
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Rephrasing failed: {response.text}"

# Main bot function
def faq_bot(user_question):
    matched_q, matched_a = search_faq(user_question)
    rephrased = rephrase_with_deepseek(user_question, matched_a)
    return f"🔎 Matched FAQ:\nQ: {matched_q}\n\n💬 Rephrased Answer:\n{rephrased}"

# Gradio app
gr.Interface(
    fn=faq_bot,
    inputs=gr.Textbox(label="Ask your question", placeholder="e.g. How do I reset my PIN?"),
    outputs="text",
    title="💬 HDFC FAQ Assistant",
    description="Ask your questions about HDFC."
).launch()

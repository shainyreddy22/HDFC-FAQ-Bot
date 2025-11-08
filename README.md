# 💬 HDFC FAQ Bot — Semantic Search + LLM Rephrasing

This project is an intelligent FAQ assistant built using:
- **FAISS** for semantic retrieval
- **Sentence Transformers** for embeddings
- **DeepSeek R1 (via OpenRouter)** for polite, rephrased answers
- **Gradio** for a clean and interactive UI

Ask questions like:  
> _"How do I reset my password?"_  
> _"Where do I register for autopay?"_

And get natural, helpful responses powered by a local FAQ dataset.

---

## 🚀 Demo

👉 Hosted on Hugging Face Spaces:  
[https://huggingface.co/spaces/abhisathvik/faq_bot](#)  

---

## 📂 Project Structure

faq_chatbot/

├── app.py # Gradio app with FAISS + DeepSeek

├── faq_data.pkl # Q&A pairs

├── faq_index.faiss # Vector index using FAISS

├── requirements.txt # Project dependencies

└── README.md # Project overview (this file)


---

## 🧠 How It Works

1. **Embedding**: All FAQ questions are embedded using `all-MiniLM-L6-v2`.
2. **Search**: On user query, the closest matching FAQ is found via FAISS.
3. **Rephrasing**: The answer is optionally reworded using DeepSeek R1 via OpenRouter API.
4. **UI**: Everything is wrapped in an interactive Gradio app.

---

## 🛠️ Run Locally

### 1. Clone this repo
  bash:
  
     git clone https://github.com/abhisathvik/faq_chatbot.git
     
     cd faq_chatbot
     
### 2. Install requirements
  bash:
  
    pip install -r requirements.txt
### 3. Set OpenRouter API Key
  Create a .env file:
  
  OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxx

### 4. Launch the app
  bash:
  
    python app.py


## 📜 License
This project is for educational and demo purposes. Not affiliated with HDFC.

## 🙌 Credits
FAISS

Sentence-Transformers

OpenRouter

Gradio

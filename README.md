
# 🤖 Hugging Face Chatbot (Streamlit App)

This is a lightweight, conversational chatbot app built with **Streamlit** and powered by the **Meta LLaMA 3.2-11B-Vision-Instruct** model via the **Hugging Face Inference API**.

---

## 👤 Author
- Andrés Evans
- linkedin.com/in/andresevans

---

## 🌐 Live Demo

Check out the live version on **Streamlit Cloud**:  
🔗 [https://chat-simulator.streamlit.app/](https://chat-simulator.streamlit.app/)

## 📦 Features

- 💬 Chat-style conversation using Hugging Face LLMs
- ⚡ Fast deployment with minimal dependencies
- 🔐 Uses Streamlit secrets management to keep your API keys safe
- 🌍 Supports natural question-answering for general knowledge

---

## 🛠️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/aevans32/streamlit-chat-simulator.git
cd streamlit-chat-simulator
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Add your secrets

Create a file named `.streamlit/secrets.toml`:

```toml
HF_API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-11B-Vision-Instruct"
HF_API_TOKEN = "your_huggingface_token"
```

### 4. Run the app
```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
streamlit-chat-simulator/
├── .streamlit/
│   └── secrets.toml         # API keys (not committed to Git)
├── main.py                  # Streamlit chatbot app
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 🧠 LLM Model Info

Model: [`meta-llama/Llama-3.2-11B-Vision-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)  
Provider: Hugging Face Inference API

Note: This model sometimes autocompletes or over-generates. It’s useful for demos, exploration, and light Q&A.

---

## 📌 Streamlit Cloud Deployment

To deploy:
1. Fork this repo
2. Connect it to [Streamlit Cloud](https://streamlit.io/cloud)
3. Set your `HF_API_TOKEN` and `HF_API_URL` under **App Settings → Secrets**

---

## 🧪 Future Ideas

- Integrate Neo4j for structured Q&A
- Shorten LLM responses dynamically
- Add image or voice input
- Use local inference (Transformers) for full control

---

## 📄 License

This project is licensed under the MIT License.

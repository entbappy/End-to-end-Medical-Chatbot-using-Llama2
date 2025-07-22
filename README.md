# 🩺 End-to-End Medical Chatbot using LLaMA 2

Build a locally hosted chatbot that uses the **LLaMA 2 model** to answer medical questions intelligently. This project uses **LangChain**, **Flask**, and **Pinecone** for backend logic and vector storage.

---

## 🚀 How to Run This Project (Step-by-Step)

### ✅ 1. Clone the Project Repository

Click the green "Code" button on GitHub, or run:

```bash
git clone https://github.com/your-repo-url
cd End-to-end-Medical-Chatbot-using-Llama2
```

---

### ✅ 2. Create a Python Environment

Make sure you have **Anaconda** or **Miniconda** installed. Then run:

```bash
conda create -n mchatbot python=3.8 -y
conda activate mchatbot
```

---

### ✅ 3. Install Required Python Libraries

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Set Up Your Pinecone API Keys

Create a file named `.env` in the **root directory** (same folder as app.py), and paste your Pinecone API info like this:

```env
PINECONE_API_KEY=your_api_key_here
PINECONE_API_ENV=your_environment_here
```

> 🔑 You can get these keys by signing up at [pinecone.io](https://www.pinecone.io/).

---

### ✅ 5. Download the LLaMA 2 Model File

1. Go to this Hugging Face page:
   👉 [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

2. Download the file:
   `llama-2-7b-chat.ggmlv3.q4_0.bin`

3. Put the downloaded file inside the `model/` directory of this project.

---

### ✅ 6. Build the Vector Index

Run the following script to prepare the chatbot’s knowledge base:

```bash
python store_index.py
```

---

### ✅ 7. Start the Chatbot App

```bash
python app.py
```

---

### ✅ 8. Open the Chatbot in Your Browser

Go to:

```bash
http://localhost:5000
```

Start chatting! 💬

---

## 🧰 Tech Stack Used

* **Python** – Backend logic
* **LangChain** – Handles LLM chains and prompts
* **Flask** – Lightweight web server
* **LLaMA 2** – Open-source LLM from Meta
* **Pinecone** – Vector database for semantic search

---

## ❓ Need Help?

Feel free to open an issue or reach out if you get stuck. Happy building! 🧠💻

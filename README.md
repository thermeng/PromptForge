<h1 align="center">🤖 PromptForge</h1>

<p align="center">
  <b>A minimal, fast, multi-model AI assistant you control</b>
</p>

<p align="center">
  Switch models • Stream responses • Keep it simple
</p>

---

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/Streamlit-App-red" />
  <img src="https://img.shields.io/badge/AutoGen-Agent-green" />
  <img src="https://img.shields.io/badge/OpenRouter-API-purple" />

  <br/>

  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/status-active-success" />

</p>

## ✨ Features

- 💬 Chat-style interface (like ChatGPT, Gemini)
- ⚡ Streaming responses
- 🔄 Switch between models:
  - google/gemma-3-27b-it
  - nvidia/nemotron-3-super-120b-a12b:free
  - You can add more...
- 🧹 Clear chat option

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

---

### 2. Create virtual environment
```bash
python -m venv .venv
```
Activate it:

Windows  
```bash
.venv\Scripts\activate  
```
Mac/Linux  
```bash
source .venv/bin/activate  
```
---

### 3. Install dependencies
```bash
pip install streamlit pyautogen python-dotenv autogen-ext[openai]
```
---

### 4. Create `.env` file
```
OPENROUTER_API_KEY=your_api_key_here  
OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"  
```
---

### 5. Run the app
```bash
streamlit run app.py
```
---

## 🧠 Models Used

This app uses models via OpenRouter:

- Gemma 3 (27B) → Fast, lightweight  
- Nemotron 3 Super (120B) → Strong reasoning  

---

## 📌 Notes

- Some models may not stream token-by-token (depends on provider)
- Responses may include artifacts like TERMINATE (model-specific)

---

## 🚀 Future Improvements

- Code review mode  
- File upload support  
- Multi-agent workflows  
- Download responses / code  

# 🤖 AgentFlow AI: Advanced Document RAG System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentflowai.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-white)](https://python.langchain.com/)

**AgentFlow AI** is a highly modular, agentic Retrieval-Augmented Generation (RAG) web application. It ingests complex documents (PDFs, Web URLs) and uses an intelligent agent-based graph system to retrieve, synthesize, and provide highly accurate answers to user queries through a sleek, dark-themed interface.

👉 **[Try the Live Application Here!](https://agentflowai.streamlit.app/)**

---

## ✨ Key Features

* **🧠 Agentic Workflow:** Utilizes a state-based graph architecture (Nodes, State, Graph Builder) for advanced reasoning rather than basic linear retrieval.
* **📄 Multi-Source Ingestion:** Seamlessly processes both local files (like PDFs) and remote URLs.
* **⚡ Blazing Fast UI:** Built with Streamlit, featuring a custom "Deep Tech" dark mode gradient interface.
* **🔍 Transparent Sourcing:** Every answer includes an expandable section showing the exact source references and document chunks used.
* **☁️ Cloud Ready:** Pre-configured for immediate deployment on Streamlit Community Cloud with secure environment variable injection.

---

## 🏗️ Project Architecture

The codebase is built with strict modularity in mind, separating the UI from the underlying AI engine:

```text
📦 DOCRAG
┣ 📂 data/                   # Document storage
┃ ┣ 📄 attention.pdf         # Sample indexed document
┃ ┗ 📄 url.txt               # List of URLs to scrape
┣ 📂 src/                    # Core RAG Engine
┃ ┣ 📂 config/               # System and LLM configurations
┃ ┣ 📂 document_ingestion/   # PDF parsing & web scraping logic
┃ ┣ 📂 graph_builder/        # LangGraph / Agentic workflow setup
┃ ┣ 📂 nodes/                # Execution nodes for the agent
┃ ┣ 📂 state/                # State management for graph traversal
┃ ┣ 📂 vectorstore/          # Embeddings and Chroma/FAISS indexing
┃ ┗ 📜 __init__.py 
┣ 📜 streamlitapp.py         # Main UI Entrypoint (Run this!)
┣ 📜 pyproject.toml          # Modern package management
┣ 📜 uv.lock                 # Lockfile for reproducible builds
┗ 📜 requirements.txt        # Standard dependency list
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Orchestration:** LangChain & LangGraph
* **LLM Provider:** Groq (Llama-3 Models)
* **Search Integration:** Tavily
* **Embeddings:** HuggingFace / OpenAI
* **Package Management:** `uv`

---

## 🚀 Quickstart (Local Development)

Want to run this system on your own machine? Follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/Tewari-Kartik/AgentFlow.git](https://github.com/Tewari-Kartik/AgentFlow.git)
cd AgentFlow
```

### 2. Set Up the Environment
You can install dependencies using standard `pip` or using `uv` (recommended):

```bash
# Using standard pip
python -m venv .venv
source .venv/Scripts/activate  # Windows users: .venv\Scripts\activate
pip install -r requirements.txt

# OR using uv (faster)
uv sync
```

### 3. Configure API Keys
Create a `.env` file in the root directory. **(Do not commit this file!)**

```env
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
```

### 4. Launch the App
```bash
streamlit run streamlitapp.py
```

---

## 👨‍💻 About the Author
Built by **Kartik Tewari**, a second-year Computer Science student based in Kanpur, Uttar Pradesh. Proud member of the APS Club, exploring the frontiers of Machine Learning, Deep Learning, and building performant agentic systems.

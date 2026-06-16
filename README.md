<div align="center">

# 🤖 AgentFlow AI

**Advanced Agentic Retrieval-Augmented Generation (RAG) System**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentflowai.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-white)](https://python.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-Fast_AI-f55036.svg)](https://groq.com/)

[Try the Live Application Here!](https://agentflowai.streamlit.app/)

</div>

---

**AgentFlow AI** is a highly modular, agentic Retrieval-Augmented Generation (RAG) web application. It ingests complex documents (PDFs, Web URLs) and uses an intelligent agent-based graph system to retrieve, synthesize, and provide highly accurate answers to user queries through a sleek, dark-themed interface.

## ✨ Key Features

* **🧠 Agentic Workflow:** Utilizes a state-based LangGraph architecture for advanced reasoning, routing, and decision-making.
* **📄 Multi-Source Ingestion:** Seamlessly processes both local files and remote URLs.
* **⚡ Blazing Fast UI:** Built with Streamlit, featuring a custom "Deep Tech" dark mode gradient interface.
* **🔍 Transparent Sourcing:** Expandable sections showing exact source references and document chunks used.
* **☁️ Cloud Ready:** Pre-configured for immediate deployment on Streamlit Community Cloud.

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interactive Chat UI & Dashboard |
| **Orchestration** | LangChain & LangGraph | Agent Workflow & Graph State |
| **LLM Provider** | Groq (Llama-3) | High-speed Inference |
| **Search** | Tavily | Real-time Web Context |
| **Package Mgr** | uv | Fast dependency resolution |

---

## 🏗️ Project Architecture

~~~text
📦 AgentFlow
┣ 📂 data/                   # Local document storage
┣ 📂 src/                    # Core RAG Engine
┃ ┣ 📂 config/               # System and LLM configurations
┃ ┣ 📂 document_ingestion/   # PDF parsing & web scraping
┃ ┣ 📂 graph_builder/        # LangGraph workflow setup
┃ ┣ 📂 nodes/                # Execution nodes for the agent
┃ ┣ 📂 state/                # State management
┃ ┗ 📂 vectorstore/          # Embeddings and indexing
┣ 📜 streamlitapp.py         # Main UI Entrypoint
┣ 📜 pyproject.toml          # Modern Python package management
┣ 📜 uv.lock                 # Lockfile for reproducible builds
┗ 📜 requirements.txt        # Standard dependency fallback
~~~

---

## 🚀 Quickstart (Local Development)

### 1. Clone the Repository
~~~bash
git clone https://github.com/Tewari-Kartik/AgentFlow.git
cd AgentFlow
~~~

### 2. Set Up the Environment
~~~bash
# Using standard pip
python -m venv .venv
source .venv/Scripts/activate  # Windows users: .venv\Scripts\activate
pip install -r requirements.txt

# OR using uv (faster)
uv sync
~~~

### 3. Configure API Keys
Create a `.env` file in the root directory. **(Do not commit this file!)**
~~~env
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
~~~

### 4. Launch the App
~~~bash
streamlit run streamlitapp.py
~~~

---

<div align="center">

### 👨‍💻 About the Author
Built by **Kartik Tewari** | Second-year Computer Science student based in Kanpur, Uttar Pradesh.  | Exploring the frontiers of Machine Learning, Deep Learning, and Agentic Systems.

</div>

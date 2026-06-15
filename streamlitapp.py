"""Streamlit UI for Agentic RAG System - Deep Tech Dark Version"""

import streamlit as st
from pathlib import Path
import sys
import time

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.config.config import Config
from src.document_ingestion.document_processor import DocumentProcessor
from src.vectorstore.vectorstore import VectorStore
from src.graph_builder.graph_builder import GraphBuilder

# Page configuration
st.set_page_config(
    page_title="Agentic RAG Search",
    page_icon="🤖",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Enhanced Modern CSS with Deep Tech Dark Background
st.markdown("""
    <style>
    /* Main App Background Gradient - Deep Tech */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff; /* Ensures text stays readable */
    }
    
    /* Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #0a1118;
    }

    /* Improved Button Styling */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.4);
    }
    .stButton > button:active {
        transform: translateY(0px);
    }
    
    /* Input field enhancement for Dark Theme */
    .stTextInput > div > div > input {
        border-radius: 8px;
        padding: 0.75rem;
        border: 1px solid #4a6fa5;
        background-color: rgba(10, 17, 24, 0.6); /* Translucent dark background */
        color: white;
    }
    
    /* Subtle container styling for headers adapted for dark mode */
    .st-emotion-cache-16idsys p {
        font-size: 1.1rem;
        color: #cccccc; /* Lighter grey for readability on dark background */
    }
    </style>
""", unsafe_allow_html=True)

def init_session_state():
    """Initialize session state variables"""
    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = None
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'num_chunks' not in st.session_state:
        st.session_state.num_chunks = 0

@st.cache_resource
def initialize_rag():
    """Initialize the RAG system (cached)"""
    try:
        # Initialize components
        llm = Config.get_llm()
        doc_processor = DocumentProcessor(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        vector_store = VectorStore()
        
        # Use default URLs
        urls = Config.DEFAULT_URLS
        
        # Process documents
        documents = doc_processor.process_urls(urls)
        
        # Create vector store
        vector_store.create_vectorstore(documents)
        
        # Build graph
        graph_builder = GraphBuilder(
            retriever=vector_store.get_retriever(),
            llm=llm
        )
        graph_builder.build()
        
        return graph_builder, len(documents)
    except Exception as e:
        st.error(f"Failed to initialize: {str(e)}")
        return None, 0

def main():
    """Main application"""
    init_session_state()
    
    # --- SIDEBAR UI ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/8649/8649605.png", width=60) # Placeholder AI Icon
        st.title("System Status")
        
        # Initialize system logic tucked neatly in the sidebar
        if not st.session_state.initialized:
            with st.status("Initializing RAG Engine...", expanded=True) as status:
                st.write("Loading configuration...")
                rag_system, num_chunks = initialize_rag()
                
                if rag_system:
                    st.session_state.rag_system = rag_system
                    st.session_state.initialized = True
                    st.session_state.num_chunks = num_chunks
                    status.update(label="System Ready!", state="complete", expanded=False)
        else:
            st.success("✅ Engine Online")
            st.metric("Documents Indexed", st.session_state.num_chunks)
            
        st.markdown("---")
        
        # History in Sidebar
        st.markdown("### 📜 Recent Queries")
        if not st.session_state.history:
            st.info("No searches yet. Ask a question to get started!")
        else:
            for item in reversed(st.session_state.history[-5:]):  # Show last 5
                with st.expander(f"Q: {item['question'][:30]}...", expanded=False):
                    st.markdown(f"**A:** {item['answer'][:150]}...")
                    st.caption(f"⏱️ {item['time']:.2f}s")

    # --- MAIN CONTENT AREA ---
    # Centered column layout for better readability on wide screens
    col1, col2, col3 = st.columns([1, 8, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center;'>🤖 AI Knowledge Assistant</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; margin-bottom: 2rem; color: #cccccc;'>Query your indexed documents with natural language</p>", unsafe_allow_html=True)
        
        # Search interface wrapped in a clean container
        with st.container(border=True):
            with st.form("search_form", clear_on_submit=False):
                question = st.text_input(
                    "What would you like to know?",
                    placeholder="e.g., Explain the core architecture of...",
                    label_visibility="collapsed"
                )
                
                # Align button nicely
                submit_col1, submit_col2, submit_col3 = st.columns([3, 2, 3])
                with submit_col2:
                    submit = st.form_submit_button("🔍 Search Documents")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # Process search
        if submit and question:
            if not st.session_state.initialized:
                st.warning("Please wait for the system to finish initializing.")
            elif st.session_state.rag_system:
                
                # Show the user's question using Streamlit's native chat UI
                with st.chat_message("user"):
                    st.write(question)
                
                with st.chat_message("assistant"):
                    with st.spinner("Analyzing documents..."):
                        start_time = time.time()
                        
                        # Get answer
                        result = st.session_state.rag_system.run(question)
                        elapsed_time = time.time() - start_time
                        
                        # Add to history
                        st.session_state.history.append({
                            'question': question,
                            'answer': result['answer'],
                            'time': elapsed_time
                        })
                        
                        # Display answer
                        st.markdown(result['answer'])
                        st.caption(f"⚡ Retrieved & synthesized in {elapsed_time:.2f} seconds")
                        
                        # Show retrieved docs in a polished expander
                        with st.expander("📄 View Source References", expanded=False):
                            for i, doc in enumerate(result['retrieved_docs'], 1):
                                st.markdown(f"**Reference {i}**")
                                st.info(doc.page_content[:400] + "...")
                                st.divider()

if __name__ == "__main__":
    main()
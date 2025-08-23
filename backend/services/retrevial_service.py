import hashlib
from typing import Dict, Tuple
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# In-memory retriever cache keyed by transcript hash (no DB)
_retriever_cache: Dict[str, FAISS] = {}

def hash(text: str) -> str:
    """Generate a hash for the given text."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def retriver(transcript_text: str):
    key = hash(transcript_text)
    if key in _retriever_cache:
        return _retriever_cache[key].as_retriever(search_type="similarity", search_kwargs={"k": 4})
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.create_documents([transcript_text])
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )
    
    vector_store = FAISS.from_documents(docs, embeddings)
    _retriever_cache[key] = vector_store
    
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})


    
    
    
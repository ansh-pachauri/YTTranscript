from typing import Tuple, List
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv

load_dotenv()


def answer_with_context(retriver, question: str) -> Tuple[str, List[str]]:
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    retriver_docs = retriver.invoke(question)
    context = "\n".join(doc.page_content for doc in retriver_docs)
    
    prompt = PromptTemplate.from_template(
        "You are a helpful assistant. Answer ONLY using the provided transcript excerpts. "
        "If the context is insufficient, say you don't know.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3,
        max_retries=2,
    )
    
    final = prompt.invoke({"context": "\n\n".join(context), "question": question})
    answer = llm.invoke(final)
    return answer.content, context
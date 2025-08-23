from typing import Tuple, List
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def answer_with_context(retriver, question: str) -> Tuple[str, List[str]]:
    
    retriver_docs = retriver.invoke(question)
    context = "\n".join(doc.page_content for doc in retriver_docs)
    
    prompt = PromptTemplate.from_template(
        "You are a helpful assistant. Answer ONLY using the provided transcript excerpts. "
        "If the context is insufficient, say you don't know.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        max_retries=2,
    )
    
    final = prompt.invoke({"context": "\n\n".join(context), "question": question})
    answer = llm.invoke(final)
    return answer.content, context
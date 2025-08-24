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
        """You are an expert YouTube transcript analyzer and video content assistant. Your role is to help users understand and navigate video content by analyzing the provided transcript excerpts.

        IMPORTANT RULES:
        1. Answer ONLY using the information provided in the transcript excerpts above
        2. If the transcript doesn't contain enough information to answer the question, say "I don't have enough information from the transcript to answer this question accurately"
        3. Be concise but thorough in your responses
        4. When referencing specific parts of the video, mention approximate timestamps if available
        5. If asked about specific topics, concepts, or people, only mention them if they appear in the transcript
        6. Do not make assumptions or add information not present in the transcript

        Context from video transcript:
        {context}

        User Question: {question}

        Please provide a clear, accurate answer based solely on the transcript information above."""
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
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
from datetime import datetime
from services.transcript_service import fetch_transcript_text
from services.retrevial_service import retriver
from services.llm_service import answer_with_context
import logging

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI backend service",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Message(BaseModel):
    text: str
    timestamp: Optional[datetime] = None

class QueryRequest(BaseModel):
    video_id: str
    question: str

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    service: str

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!", "status": "running"}

# Health check endpoint
@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        service="FastAPI Project"
    )

# Example message endpoint
@app.post("/ask")
def ask_question(req: QueryRequest):
    transcript = fetch_transcript_text(req.video_id)
    print("Transcripted fetched")
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")
    
    retriv_transcript = retriver(transcript)
    print("Retriever created")
    try:
        answer, context = answer_with_context(retriv_transcript, req.question)
        return {
            "answer": answer,
            "context": context
        }
        
    except Exception as e:  
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")  

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

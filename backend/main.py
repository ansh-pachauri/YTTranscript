from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
from datetime import datetime

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
@app.post("/message", response_model=Message)
async def create_message(message: Message):
    if not message.timestamp:
        message.timestamp = datetime.now()
    return message

# Get current time
@app.get("/time")
async def get_time():
    return {"current_time": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

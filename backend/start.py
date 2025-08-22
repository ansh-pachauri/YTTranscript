#!/usr/bin/env python3
"""
Startup script for FastAPI application
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting FastAPI application...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔍 Alternative Docs: http://localhost:8000/redoc")
    print("❤️  Health Check: http://localhost:8000/health")
    print("-" * 50)
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

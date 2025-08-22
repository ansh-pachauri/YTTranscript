# FastAPI Project

A clean, simple FastAPI backend service with basic endpoints and automatic API documentation.

## 🚀 Features

- **FastAPI framework** with automatic API documentation
- **CORS middleware** for frontend integration
- **Pydantic models** for request/response validation
- **Health check endpoints** for monitoring
- **Interactive API testing** via Swagger UI
- **Hot reload** for development

## 📁 Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── start.py             # Startup script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🛠️ Setup

### 1. **Navigate to the backend directory**
```bash
cd backend
```

### 2. **Create a virtual environment**
```bash
python -m venv venv
```

### 3. **Activate the virtual environment**
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

### **Option 1: Using the startup script (Recommended)**
```bash
python start.py
```

### **Option 2: Direct execution**
```bash
python main.py
```

### **Option 3: Using uvicorn directly**
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## 🌐 Accessing Your API

Once running, your API will be available at:

- **API Root**: `http://localhost:8000/`
- **Interactive API Docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API Docs (ReDoc)**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 📋 Available Endpoints

### **Core Endpoints**
- `GET /` - Welcome message and status
- `GET /health` - Health check with timestamp
- `GET /time` - Current server time

### **Data Endpoints**
- `POST /message` - Create a new message

## 🧪 Testing Your API

### **Using the Interactive GUI (Swagger UI)**
1. Open `http://localhost:8000/docs` in your browser
2. Click on any endpoint to expand it
3. Click "Try it out" to test the endpoint
4. Fill in any required parameters
5. Click "Execute" to see the response

### **Example API Calls**

#### **Test the root endpoint:**
```bash
curl http://localhost:8000/
```

#### **Test the health check:**
```bash
curl http://localhost:8000/health
```

#### **Test the message endpoint:**
```bash
curl -X POST "http://localhost:8000/message" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, FastAPI!"}'
```

## 🔧 Configuration

The application runs on:
- **Host**: `127.0.0.1` (localhost)
- **Port**: `8000`
- **Reload**: Enabled for development

## 📚 Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## 🚀 Next Steps

1. **Add more endpoints** for your specific use case
2. **Implement database integration** (SQLAlchemy, etc.)
3. **Add authentication and authorization**
4. **Implement logging and monitoring**
5. **Add tests with pytest**
6. **Set up CI/CD pipeline**

## 🐛 Troubleshooting

### **Common Issues**

1. **Port already in use**: Change the port in `main.py` or kill the process using port 8000
2. **Import errors**: Make sure your virtual environment is activated
3. **Dependencies not found**: Run `pip install -r requirements.txt` again

### **Getting Help**

- Check the console output for error messages
- Review the API docs at `/docs` when the server is running
- Check the FastAPI documentation for best practices

---

**Happy coding! 🎉**

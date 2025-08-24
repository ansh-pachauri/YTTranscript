# 🎥 YT Transcript Assistant

<div align="center">

![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-v1.0-blue?logo=google-chrome&logoColor=white)
![AI Powered](https://img.shields.io/badge/AI%20Powered-Gemini%202.5%20Flash-green?logo=google)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-red?logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React%20+%20TypeScript-blue?logo=react)

**Your AI-powered YouTube transcript companion that helps you understand, navigate, and extract insights from video content.**

[⭐ Star this repo](https://github.com/ansh-pachauri/YTTranscript)

</div>

---

## ✨ What Can This Bot Do?

The **YT Transcript Assistant** is a powerful Chrome extension that transforms how you interact with YouTube videos. Here's what makes it special:

### 🧠 **AI-Powered Analysis**
- **Smart Q&A**: Ask questions about video content and get intelligent, contextual answers
- **Content Summarization**: Get concise summaries of video sections or entire content
- **Key Point Extraction**: Identify and highlight important concepts and takeaways
- **Timestamp Navigation**: Find specific moments in videos based on your queries

### 🎯 **Transcript Intelligence**
- **Automatic Detection**: Seamlessly detects YouTube video IDs from any YouTube page
- **Real-time Processing**: Analyzes transcripts using advanced AI models
- **Context-Aware Responses**: Provides answers based solely on actual video content
- **Beautiful Formatting**: Responses are formatted with markdown for easy reading

### 🚀 **User Experience**
- **Chrome Extension**: Works directly in your browser - no need to copy/paste URLs
- **Instant Access**: Click the extension icon on any YouTube page to start chatting
- **Responsive Design**: Clean, modern interface that adapts to your needs
- **Real-time Chat**: Interactive conversation with your video content

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Chrome       │    │   React          │    │   FastAPI       │
│   Extension    │◄──►│   Frontend       │◄──►│   Backend       │
│   (Popup)      │    │   (TypeScript)   │    │   (Python)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
   YouTube Page           Beautiful UI            Gemini AI API
   Detection              Components              Processing
```

---

## 🛠️ Tech Stack

### **Frontend (Chrome Extension)**
- **React 18** with TypeScript for robust development
- **Tailwind CSS** for beautiful, responsive styling
- **Chrome Extension APIs** for YouTube integration
- **Axios** for HTTP communication

### **Backend (AI Service)**
- **FastAPI** for high-performance API endpoints
- **LangChain** for AI workflow orchestration
- **Google Gemini 2.5 Flash** for intelligent responses
- **Vector Search** for context-aware transcript retrieval

### **AI & Processing**
- **Advanced Prompt Engineering** for accurate responses
- **Context-Aware Retrieval** for relevant information
- **Markdown Formatting** for beautiful response display

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+ installed
- Node.js 16+ installed
- Chrome browser
- Google AI API key

### **1. Clone the Repository**
```bash
git clone https://github.com/ansh-pachauri/YTTranscript
cd YTTranscript
```

### **2. Backend Setup**
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set your Google AI API key
# Create .env file and add:
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Start the backend server
python start.py
```

### **3. Frontend Setup**
```bash
# Navigate to frontend directory
cd yt-frontend

# Install dependencies
npm install

# Build the extension
npm run build
```

### **4. Load Chrome Extension**
1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (top right toggle)
3. Click "Load unpacked"
4. Select the `yt-frontend/dist` folder
5. The extension icon should appear in your toolbar

### **5. Start Using**
1. Go to any YouTube video
2. Click the extension icon
3. Start asking questions about the video content!

---

## 🔧 Configuration

### **API Configuration**
The extension connects to your local backend by default. To change the API endpoint:

1. **Edit the API URL** in `yt-frontend/src/App.tsx`:
```typescript
// Change this line (around line 61)
const res = await axios.post("http://localhost:8000/ask", {
  // ... your data
})
```

2. **Update CORS settings** in `backend/main.py` if needed:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### **Environment Variables**
Create a `.env` file in the `backend/` directory:
```env
GOOGLE_API_KEY=your_google_ai_api_key_here
```

---

## 📱 How It Works

### **1. Video Detection**
- Extension automatically detects when you're on a YouTube page
- Extracts video ID and fetches video title
- No manual copying/pasting required

### **2. AI Processing**
- Your question is sent to the backend
- AI retrieves relevant transcript segments
- Gemini 2.5 Flash generates contextual responses
- Responses are formatted with beautiful markdown

### **3. Smart Responses**
- **Bold text** for key concepts
- **Bullet points** for lists
- **Code formatting** for technical terms
- **Blockquotes** for important statements
- **Timestamps** when available

---

## 🎯 Use Cases

### **For Students**
- **Study Aid**: Ask questions about educational content
- **Note Taking**: Extract key points and summaries
- **Research**: Find specific information in long videos

### **For Professionals**
- **Training Videos**: Understand complex procedures
- **Meeting Recordings**: Extract action items and decisions
- **Product Demos**: Get quick answers about features

### **For Content Creators**
- **Content Analysis**: Understand what others are saying
- **Research**: Find relevant information in competitor videos
- **Fact Checking**: Verify claims made in videos

---

## 🔒 Privacy & Security

- **Local Processing**: All AI processing happens on your backend
- **No Data Storage**: Transcripts are processed in real-time, not stored
- **Secure API**: Uses your own Google AI API key
- **Chrome Permissions**: Only accesses YouTube pages when active

---

## 🚀 Future Enhancements

- [ ] **Multi-language Support** for international videos
- [ ] **Voice Commands** for hands-free interaction
- [ ] **Export Features** for saving conversations
- [ ] **Batch Processing** for multiple videos
- [ ] **Advanced Analytics** for content insights
- [ ] **Mobile App** for on-the-go access

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### **Development Guidelines**
- Follow TypeScript best practices
- Use meaningful commit messages
- Test your changes thoroughly
- Update documentation as needed

---

## 🐛 Troubleshooting

### **Common Issues**

| Issue | Solution |
|-------|----------|
| Extension not loading | Check if `npm run build` completed successfully |
| API connection failed | Verify backend is running on port 8000 |
| No video detected | Ensure you're on a YouTube video page |
| AI responses slow | Check your internet connection and API key |

### **Debug Mode**
Enable debug logging in the extension:
1. Right-click extension icon
2. Select "Inspect popup"
3. Check console for error messages

---

## 📚 API Reference

### **Backend Endpoints**

#### `POST /ask`
Ask a question about a video transcript.

**Request Body:**
```json
{
  "question": "What are the main points discussed?",
  "video_id": "dQw4w9WgXcQ"
}
```

**Response:**
```json
{
  "answer": "Based on the transcript, the main points discussed are...",
  "context": "Relevant transcript segments..."
}
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful language processing
- **FastAPI** for the excellent backend framework
- **React Team** for the amazing frontend library
- **Chrome Extension APIs** for seamless browser integration

---


<div align="center">

**Made with ❤️ by [Ans Pachauri]**

[⭐ Star this repo](https://github.com/ansh-pachauri/YTTranscript) • [🚀 Get Started](#-quick-start) • [📖 Learn More](#-what-can-this-bot-do)

</div>

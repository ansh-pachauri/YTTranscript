
import { MessageSquare, Send } from 'lucide-react'
import './App.css'
import { Card } from './components/ui/card'
import { ScrollArea } from './components/ui/scroll-area'
import React, { useRef, useState } from 'react'
import { Input } from './components/ui/input'
import { Button } from './components/ui/button'
import axios from 'axios'


interface Message {
  id: string
  type: 'bot' | 'user'
  content: string
  timestamp: Date
}

function App() {

  const [messages, setMessages] = useState<Message[]>([
    {
      "id": '1',
      type: "bot",
      content:
        "Hi! I'm your video transcript assistant. I can help you find specific moments, summarize content, or answer questions about this video. What would you like to know?",
      timestamp: new Date(),
    },
  ])

  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const [videoId, setVideoId] = useState<string>('')

  // handle key pressing
  const handlekeyPress = (e: React.KeyboardEvent) =>{
    if(e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  // handle sending message
  const handleSendMessage =async() =>{
    if(!inputValue.trim() || isLoading) return

    const userMessage: Message = {
      id: Date.now().toString(),
      type: "user",
      content: inputValue,
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)

    try{
      const res = await axios.post("http://localhost:8000/ask",{
        question: inputValue,
        video_id: videoId
        
      })
      const data = res.data;

      setTimeout(() =>{
        const botMessage: Message = {
          id: Date.now().toString(),
          type: "bot",
          content: data.answer,
          timestamp: new Date(),
        }
  
        setMessages((prev) => [...prev, botMessage])
        setIsLoading(false)
      },1000)
      
    }

    catch (error) {
      console.error("Error sending message:", error)
      setIsLoading(false)
      const errorMessage: Message = {
        id: Date.now().toString(),
        type: "bot",
        content: "Sorry, I couldn't process your request. Please try again later.",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
    }

  }

  // Auto detect video id from current tab
  React.useEffect(() => {
    if (typeof chrome !== 'undefined' && chrome.tabs) {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs[0]?.url) {
          const url = new URL(tabs[0].url);
          let vid = '';
          
          // Handle different YouTube URL formats
          if (url.hostname.includes('youtube.com')) {
            vid = url.searchParams.get('v') || '';
          } else if (url.hostname.includes('youtu.be')) {
            vid = url.pathname.slice(1); // Remove leading slash
          }
          
          setVideoId(vid);
        }
      });
    }
  }, []);

  
  

 

  return (
    <>
      <Card className='w-96 h-auto bg-card/95 backdrop-blur-sm border-border shadow-xl z-50 flex flex-col'>
      {/* Header */}
        <div className='flex items-center justify-between p-4 border-b border-border'>
          <div className='flex items-center gap-2 flex-1 min-w-0'>
            <MessageSquare className='h-5 w-5 text-primary flex-shrink-0' />
            <div className='min-w-0 flex-1'>
              <h3 className='font-semibold text-sm text-foreground truncate'>
                Video Chat
              </h3>
              {videoId}
            </div>
          </div>
        </div>

        {/* Messages section */}
        <ScrollArea className='flex-1 p-4'>
          <div className='space-y-4'>
            {messages.map((message) => (
              <div key={message.id} className={`flex ${message.type === "user" ? "justify-end" : "justify-start"}`}>
                <div
                  className={`max-w-[80%] rounded-lg p-3 ${
                    message.type === "user" ? "bg-primary text-primary-foreground" : "bg-muted text-muted-foreground"
                  }`}
                >
                  {message.content}
                  <div className='text-sm text-right opacity-70 mt-1'>
                  {message.timestamp.toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit"
                  })}
                  </div>
                </div>
              </div>
            ))
            }

            {isLoading && (
            <div className="flex justify-start">
              <div className="bg-muted text-muted-foreground rounded-lg p-3 max-w-[80%]">
                <div className="flex items-center gap-2">
                  <div className="flex gap-1">
                    <div className="w-2 h-2 bg-current rounded-full animate-bounce" />
                    <div
                      className="w-2 h-2 bg-current rounded-full animate-bounce"
                      style={{ animationDelay: "0.1s" }}
                    />
                    <div
                      className="w-2 h-2 bg-current rounded-full animate-bounce"
                      style={{ animationDelay: "0.2s" }}
                    />
                  </div>
                  <span className="text-sm">Analyzing transcript...</span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesRef} />
          </div>
        </ScrollArea>

        {/* Input block */}
        <div className='p-4 border-t border-border'>
          <div className='flex gap-2'>
            <Input
            ref={inputRef}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handlekeyPress}
            placeholder='Ask about the content og the video...'
            className="flex-1 bg-input text-foreground placeholder:text-muted-foreground"
            disabled={isLoading}

            />
            <Button
            onClick={handleSendMessage}
            disabled={!inputValue.trim() || isLoading} size="sm" className="px-3">
            <Send className="h-4 w-4" />
          </Button>

          </div>
          <p className='text-sm text-muted-foreground text-center mt-2'>
          Press Enter to send • Powered by AI 
          </p>
          <div className='border-border text-muted-foreground text-md text-center'>
            <p>• Build by Ansh</p>
          </div>
        </div>
      </Card>
    </>
  )
}

export default App

**CYBER_BUDDY** 

> AI-powered voice assistant for hands-free cybersecurity research

---

**## Introduction**

CYBER_BUDDY is a voice-activated AI assistant designed for cybersecurity professionals,
students, and researchers. It enables hands-free interaction with a Large Language Model
(Google Gemini) to assist during security analysis, code review, and research workflows.

The project focuses on productivity, minimal interaction overhead, and secure handling
of sensitive environments.

---

**## How It Works**
      
      Microphone
          ↓
    Speech Recognition (STT)
          ↓
    Gemini LLM Engine
          ↓
    Text-to-Speech (macOS)
          ↓
    Audio Output
---

**## Features**

- Voice-controlled interaction
- Gemini 2.5 Flash integration
- Hands-free security analysis
- Secure API key handling via `.env`
- Thread-safe microphone and TTS handling
- Optimized for red team labs and research sessions
- Native macOS voice support

---

**## Requirements**

- macOS
- Python 3.8+
- PortAudio
- Google Gemini API key
- Working microphone

---

**## Dependencies**
    
    python-dotenv
    SpeechRecognition
    PyAudio
    google-generativeai
    pyttsx3
---

**## Installation**

    # Clone the repository:
    git clone https://github.com/Vishal-HaCkEr1910/CYBER-BUDDY-AI-VOICE-CHATBOT-.git
    cd CYBER-BUDDY-AI-VOICE-CHATBOT-
    brew install portaudio
    pip install -r requirements.txt
---

**## Configuration**
    #Create a `.env` file in the project root:
     
     GEMINI_API_KEY=your_api_key_here
Make sure `.env` is included in `.gitignore`.

---

**## Usage**
Run the assistant:

    python3 CYBER_BUDDY.py
Example startup output:
> CyberBuddy is online. I am listening.

---

**## Voice Commands**

- Speak naturally to interact with the assistant
- Ask security-related questions or code queries
- Use `exit`, `stop`, or `quit` to terminate

---

**## Security Notes**

- API keys are never hardcoded
- No persistent storage of conversations
- Audio thread locking prevents echo and race conditions
- Intended for controlled environments

---

**## Intended Use**

CYBER_BUDDY is intended for:

- Cybersecurity education
- Ethical hacking research
- Red teaming and blue teaming assistance
- AI-assisted analysis workflows

Misuse against unauthorized systems is strictly prohibited.

---

**## Project Status**

Active development  
Planned improvements include modular commands, Linux support,
and context-aware AI interactions.

---

**## Author**

**Vishal Yadav** 
**Cybersecurity Student — IIIT Una  
Focus: Red Teaming, AI in Security, Offensive Research**

---

**## License**

This project is released for educational and research purposes only.

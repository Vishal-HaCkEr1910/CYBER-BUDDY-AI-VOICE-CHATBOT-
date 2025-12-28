##########################################################################################
#                                                                                        #
#    ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗██████╗ ██████╗  ██╗   ██╗ #
#   ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗ ╚██╗ ██╔╝ #
#   ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║██║  ██║██║  ██║  ╚████╔╝  #
#   ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║  ██║██║  ██║   ╚██╔╝   #
#   ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██████╔╝██████╔╝    ██║    #
#    ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝     ╚═╝    #
#                                                                                        #
#   [ SYSTEM_ID: CYBER_BUDDY_V1.5 ]          **[ AUTHOR: VISHAL_YADAV ]**                #
#                                                                                        #
#                                                                                        #
##########################################################################################

> INITIALIZING INTERFACE...
> LOADING GEMINI_FLASH_2.5_ENGINE...
> CALIBRATING MAC_OS_RISHI_VOICE...

---[ 01. CORE_LOGIC ]----------------------------------------------------------

CYBER_BUDDY is a voice-activated LLM (Large Language Model) integration 
designed for hands-free security analysis. It bypasses the need for 
manual keyboard input during sensitive research sessions.

LOGIC_FLOW:
[VOICE_INPUT] --> [GOOGLE_STT] --> [GEMINI_LLM] --> [MAC_SAY_TTS] --> [OUT]

---[ 02. SYSTEM_REQUIREMENTS ]-------------------------------------------------

- OS     : macOS (Architecture-specific for native 'say' utility)
- KERNEL : Python 3.8+
- ASSET  : Gemini API Key (Stored in root/.env)
- REQS   : PortAudio, PyAudio, SpeechRecognition, Google-GenerativeAI

---[ 03. DEPLOYMENT_SEQUENCE ]-------------------------------------------------

[STEP_01] Clone the source:
$ git clone https://github.com/Vishal-HaCkEr1910/CYBER-BUDDY-AI-VOICE-CHATBOT-.git

[STEP_02] Install hardware bridges:
$ brew install portaudio
$ pip install -r requirements.txt

[STEP_03] Inject Credentials: (Put this inside a file named .env or just use the command below)
$ echo "GEMINI_API_KEY=your_key_here" > .env

[STEP_04] Execute Binary:
$ python3 CYBER_BUDDY.py

---[ 04. COMMANDS ]-----------------------------------------------------------

- GREETING : "CyberBuddy is online. I am listening, Vishal."
- ANALYSIS : Speak any security query or code snippet for auditing.
- TERMINATE: "Exit", "Stop", or "Quit".

---[ 05. SECURITY_INTEGRITY ]-------------------------------------------------

- API keys are handled via python-dotenv and filtered through .gitignore.
- Mic-Lock threading implemented to prevent resource deadlocks.
- Ambient noise calibration ensures high-fidelity signal capture.

---[ 06. DISCLAIMER ]---------------------------------------------------------

AUTHORIZED USE ONLY. This tool is designed for white-hat research and 
educational purposes. Unauthorized use against systems is strictly prohibited.

###############################################################################


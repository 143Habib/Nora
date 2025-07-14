🔹 **Project Name:** Nora – Your Personal Voice-Powered AI Assistant (Text Version)

🔹 **Overview:**
Nora is a lightweight Python-based AI assistant that responds to user input through both text and spoken voice. It can execute basic system commands (like opening Notepad or checking battery status) and answer natural language questions using the Groq API powered by the LLaMA 3 model. This version supports keyboard-based command input and responds using text-to-speech via `pyttsx3`.

🔹 **Key Features:**

* **Text-to-Speech Interaction**
  Uses `pyttsx3` for generating voice responses locally without internet dependency.

* **Command Input via Keyboard**
  Simulates a simple voice assistant interface using typed commands in the terminal.

* **AI-Powered Conversations**
  Connects to Groq’s `llama3-8b-8192` model for answering natural language queries.

* **Utility Commands:**

  * Launch Notepad
  * Launch Calculator
  * Take screenshots
  * Check system battery percentage

* **Fallback AI Responses:**
  When a command isn't recognized, Nora asks the Groq API for an intelligent response.

* **Terminal-Based Interface:**
  Minimal and clean interface for easy debugging and development.

🔹 **Technologies Used:**

* `Python` – Core language
* `requests` – For communicating with the Groq API
* `pyttsx3` – For local text-to-speech
* `pyautogui` – For GUI automation tasks like screenshots
* `psutil` – For monitoring battery status
* `os` – For executing system commands
* `Groq API` – For natural language understanding and intelligent responses

🔹 **What I Learned:**

* How to send and handle HTTP API requests in Python.
* Integrating multiple external libraries for building real-world tools.
* Basic command processing logic and fallback mechanism to LLM.
* Handling speech synthesis and working with system-level operations.
* Writing modular, clean, and scalable Python code.

🔹 **Future Plans:**

* Add full voice recognition support using `speech_recognition` or `Whisper`.
* Introduce scheduling features, weather updates, and file search.
* Build a GUI interface using `Tkinter` or `PyQt`.
* Support for multiple languages and customizable assistant personalities.



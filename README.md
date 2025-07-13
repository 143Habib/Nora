🔹 Project Name: Nora – Your Personal Voice-Powered AI Assistant
🔹 Overview:
Nora is my first Python-based AI assistant project, combining speech synthesis, basic command execution, and AI-generated conversational responses. Designed as a lightweight, voice-interactive desktop assistant, Nora not only handles basic tasks like opening Notepad, taking screenshots, and checking battery status but also answers general queries using the Groq API with the LLaMA 3 model.

🔹 Key Features:
🗣️ Text-to-Speech Interaction using pyttsx3 for natural voice responses.

⌨️ Command Listening Interface (via keyboard input for now) simulating voice commands.

🧠 AI-Powered Conversations via Groq’s llama3-8b-8192 model.

🛠️ Utility Commands:

Launch apps like Notepad and Calculator.

Take instant screenshots.

Check battery percentage.

🧼 Clean Interface: Terminal-based interaction for simplicity and ease of debugging.

🔹 Technologies Used:
Python

requests (for API communication)

pyttsx3 (for offline text-to-speech)

pyautogui (for GUI automation like screenshots)

psutil (for battery monitoring)

Groq API (for natural language AI responses)

🔹 What I Learned:
How to make HTTP API requests and handle responses.

Working with external libraries to interact with the OS and user input/output.

Basics of natural language processing and integrating LLMs into real-world applications.

Structuring and organizing Python scripts for scalable projects.

🔹 Future Plans:
Add actual voice recognition using speech_recognition or whisper.

Add task scheduling, weather updates, and file search functionalities.

Replace terminal input with a GUI using tkinter or PyQt.

Add multilingual support and customizable personalities.

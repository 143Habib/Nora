import requests
import pyttsx3
import pyautogui
import psutil
import os

# ------------------- CONFIG -------------------
GROQ_API_KEY = "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"  
GROQ_MODEL = "llama3-8b-8192"
# ----------------------------------------------

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    return input("Type your command here: ")

def ask_groq(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    body = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error contacting Groq API: {str(e)}"

def execute_command(command):
    command = command.lower()
    if command in ["hi", "hello", "hey"]:
        return "Hi there!"
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad."
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator."
    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot taken."
    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery is at {battery.percent}%"
        else:
            return "Sorry, could not get battery information."
    elif command in ["exit", "quit", "bye", "goodbye"]:
        speak("Goodbye! Have a nice day.")
        exit(0)
    return None

def main():
    speak("Hello.....I am Nora.....How can I help You?")
    while True:
        user_input = listen()
        local_response = execute_command(user_input)
        if local_response:
            print("🖥️ Command:", local_response)
            speak(local_response)
        else:
            response = ask_groq(user_input)
            print("Nora:", response)
            speak(response)

if __name__ == "__main__":
    main()

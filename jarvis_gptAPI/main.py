import speech_recognition as sr
import os
import win32com.client as wc
import webbrowser
import openai

speaker = wc.Dispatch("SAPI.SpVoice")

# function to make the Jarvis speak.
def say(text):
    speaker.Speak(text)

# function to convert speech into the text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis."



if __name__ == '__main__':
    say('''Hi, I'm Jarvis. Your personal A.I assistant.
            How can I help you today?''')

    query = takeCommand()
    say(query)

    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikidpedia.com"],
        ["linkedin", "https://www.linkedin.com"]
    ]

    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir ...")
            webbrowser.open(site[1])

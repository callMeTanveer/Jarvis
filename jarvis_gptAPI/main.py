import speech_recognition as sr
import os
import win32com.client as wc
import webbrowser
from aiModel import response

speaker = wc.Dispatch("SAPI.SpVoice")

# function to make the Jarvis speak.
def say(text):
    speaker.Speak(text)

# function to convert speech into the text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis."

def Pass():
    say("Hi, you will have to prove yourself as Tanveer before using me.")
    for i in range(3):
        say("What is your favourite food?")
        response = takeCommand()
        print(response.lower())
        if "chicken".lower() in response.lower() or "chilli".lower() in response.lower():
            say("Thanks for the response! Access authorized")
            return True
        else:
            if i > 0:
                say(f"You are left with {2-i} attempt.")
            else:
                say("Sorry!!")
                say("The access cannot be authorized to you. And don't dare to come again.")

    return False

def conversation():
    say("Please say qu to end the conversation.")
    quit = ""

    while True:
        query = takeCommand()
        print(query)
        jarvis_response = response(query)
        # print(jarvis_response)
        say(jarvis_response)
        say("What else I could help you with Tanveer?")




if __name__ == '__main__':
    # say('''Hi, I'm Jarvis. Your personal AI assistant.
    #         How can I help you today?''')

    greeting_message = "Hello! I'm your personal assistant. Ready to assist you with information, answer questions, and help with various tasks. Feel free to ask me anything!"
    if not Pass():
        exit()

    say(greeting_message)
    conversation()


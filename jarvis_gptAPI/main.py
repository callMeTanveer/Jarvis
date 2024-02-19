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

def user_authentication():
    say("Hi, you will have to prove yourself as Tanveer before using me.")
    for i in range(1, 4):
        say("What is your favourite food?")
        user_response = takeCommand()
        print(user_response.lower())
        if "chicken".lower() in user_response.lower() or "chilli".lower() in user_response.lower():
            say("Thanks for the response! Access authorized")
            return True
        else:
            if i < 3 :
                say(f"Wrong!! You are left with {3-i} attempt.")
            else:
                say("Sorry!!")
                say("The access cannot be authorized to you. And don't dare to come again.")

    return False

def conversation():
    # say("Please say qu to end the conversation.")
    # quit = ""

    while True:
        query = takeCommand()
        print(f"Tanveer: {query}")
        jarvis_response = response(query)
        print(f"Jarvis: {jarvis_response}")
        say(jarvis_response)
        # say("What else I could help you with Tanveer?")




if __name__ == '__main__':
    # say('''Hi, I'm Jarvis. Your personal AI assistant.
    #         How can I help you today?''')

    greeting_message = "Hello! I'm your personal assistant. Ready to assist you with information, answer questions, and help with various tasks. Feel free to ask me anything!"
    if not user_authentication():
        exit()

    say(greeting_message)
    conversation()


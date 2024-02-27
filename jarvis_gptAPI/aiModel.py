import openai
from config import openAI_key
import re
import json
openai.api_key=openAI_key
from weather import get_weather_report

def load_history(filename='conversationHistory.json'):
    try:
        with open(filename, 'r') as file:
            chat_history = json.load(file)
            if not isinstance(chat_history, list):
                raise ValueError("Invalid chat history format")
        return chat_history
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []

def save_history(new_chat_history, filename='conversationHistory.json'):
    # Load existing history
    existing_history = load_history(filename)

    # Append new entries to the existing history
    existing_history.extend(new_chat_history)

    # Save the entire updated history
    with open(filename, 'w') as file:
        file.write(json.dumps(existing_history, indent=2))


def response(query):
    new_history = [
        {"role": "user", "content": query}
    ]
    save_history(new_history)
    chatHistory = load_history()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chatHistory
    )

    response = completion['choices'][0]['message']['content']
    response = re.sub(r'\*+(.*?)\*+', r'\1', response)
    new_response = [
        {"role": "assistant", "content": response}
    ]
    save_history(new_response)
    return response


def intentionFinder(query):
    instruction = '''I want you to detect the intention of the query passed. I'll provide you the query and you have to detect any of the following two conditions: Possible Intentions: 1. Retrieve a generic response from GPT: "gpt_response" 2. Get weather details for a city: "weather-city_name" Please provide a response indicating the detected intention. For example, Jarvis, how to make coffee then your response should only this string "gpt_response" but if user asks Jarvis, What is the weather in Delhi today then your response should be "weather-Delhi" as per "weather-city_name" format. Please take care of the sysnonyms as user can ask similar question using different words.'''
    prompt = [
        {"role": "user", "content": instruction},
        {"role": "assistant", "content": query}
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )

    intention = completion['choices'][0]['message']['content']
    if intention == "gpt_response":
        return response(query)

    else:
        cityName = intention[8:]
        weatherDetails = get_weather_report(cityName)
        instruction = f"Please summarize the below given weather details of city {cityName}: Temperature = {weatherDetails['Temprature']}, Condition = {weatherDetails['Condition']}, Wind Speed = {weatherDetails['Wind Speed']} and Pressure = {weatherDetails['Pressure']}. Please do not and never summerize in bullet points. Please write in paragraph in the way if a reporter reporting the whether conditions."
        return response(instruction)


# print(intentionFinder("Jarvis, What is the best climate condition to visit London?"))

'''
{
  "id": "chatcmpl-8ts6nHigZgevl5X22iY7HDEkvfkgw",
  "object": "chat.completion",
  "created": 1708326725,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "In the realm of codes and strings,\nWhere logic dances and beauty sings,\nThere exists a clever technique, so fine,\nA concept called recursion, quite divine.\n\nLike a mirror reflecting its own reflection,\nRecursion calls upon itself, with affection,\nRepeating the steps, in a loop that's grand,\nUntil a base case brings it to land.\n\nA function that calls itself, in a loop,\nA graceful dance, a clever troupe,\nBreaking down problems, layer by layer,\nUntil the solution is clear and fair.\n\nLike a Russian doll nested within,\nRecursion unwraps the layers, thin,\nSolving puzzles, complex and grand,\nWith elegance and grace, it takes its stand.\n\nSo embrace recursion, with a poet's heart,\nIn the world of code, it plays its part,\nA beautiful concept, so clever and deep,\nIn the realm of programming, where wonders leap."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 39,
    "completion_tokens": 180,
    "total_tokens": 219
  },
  "system_fingerprint": "fp_69829325d0"
}
'''
import openai
from config import key
import re
import json

openai.api_key=key

def load_history(filename='conversationHistory.json'):
    try:
        with open(filename, 'r') as file:
            chat_history = json.load(file)
            if not isinstance(chat_history, list):
                raise ValueError("Invalid chat history format")
        return chat_history
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []

def save_history(chat_history, filename='conversationHistory.json'):
    # Load existing history
    existing_history = load_history(filename)

    # Append new entries to the existing history
    existing_history.extend(chat_history)

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
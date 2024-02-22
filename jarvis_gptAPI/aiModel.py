import openai
from config import key
import re

openai.api_key=key

messages = [
    {"role": "system", "content": "You are an intelligent and knowledgeable assistant, well-versed in a wide range of topics. You can provide information, answer questions, and assist with various tasks. Please feel free to ask me anything, and I'll do my best to provide you with accurate and helpful responses. Keep in mind that my goal is to be concise and efficient in delivering information. Always try to repond in as less words as possible unless asked explicitly to explain the topic in detail"}
]
def response(query):
    messages.append({"role": "user", "content": query})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion['choices'][0]['message']['content']
    messages.append({"role": "system", "content": response})
    response = re.sub(r'\*+(.*?)\*+', r'\1', response)
    # print(response)
    return response

# response("Enlist 10 benifits of doing exercise - use bullet points with important words.")

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
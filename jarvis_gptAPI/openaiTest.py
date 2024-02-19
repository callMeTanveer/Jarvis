import openai
from config import key

openai.api_key=key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

# Extract and print the generated message
generated_message = completion['choices'][0]['message']['content']
print(generated_message)

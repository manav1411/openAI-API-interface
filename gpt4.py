import requests
import json

API_KEY = "<your API token here>"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    print("gpt4 is generating response...")
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

#takes in the users input
user_input = []
print("your gpt4 prompt: ")
while True:
    try:
        line = input()
    except EOFError:
        break
    user_input.append(line)
concatenated_input = "\n".join(user_input)


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": concatenated_input}
]

response_text = generate_chat_completion(messages)
print("\ngpt4 response: ")
print(response_text)

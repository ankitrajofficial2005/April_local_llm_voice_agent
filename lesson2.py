import requests


url = "http://localhost:11434/api/chat"

payload ={
    "model": "qwen3.5:4b",
    "messages": [
        {
            "role": "user",
            "content": "what is python?"
        }

        
    ],
    "stream": False

}

response = requests.post(url, json=payload)
data = response.json()
print(data["message"]["content"])

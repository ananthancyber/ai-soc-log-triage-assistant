from ollama import chat

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a brute-force attack is in cybersecurity."
        }
    ]
)

print(response["message"]["content"])
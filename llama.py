from openai import OpenAI
import ollama
ask =  input("Enter  your question :")
response = ollama.chat(model = 'llama3', messages=[
    {
    'role' : 'user',
    'content' : ask,
    },
])
print(response['message']['content'])
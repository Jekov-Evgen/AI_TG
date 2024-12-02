import ollama
import asyncio

async def return_ollama(message):
    result = ollama.chat(
        model="llama3.1:latest", 
        messages=[{'role': 'user', 'content': message}]
    )

    return result.message.content
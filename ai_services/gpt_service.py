# src/ai_services/gpt_service.py

from openai import OpenAI
import os

# Create a client using your API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to get GPT-4 response
async def get_gpt_response(question: str) -> str:
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )
    return chat_completion.choices[0].message.content

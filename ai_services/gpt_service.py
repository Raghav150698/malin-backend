# ai_services/gpt_service.py

import os
from openai import AsyncOpenAI

# Create a single global async client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_gpt_response(question: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Log or return error message for debugging
        return f"GPT error: {e}"

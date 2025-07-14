# ai_services/gpt_service.py

from openai import OpenAI
import os

# Ensure you set your API key in your Render environment or .env
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def get_gpt_response(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error from GPT: {str(e)}"

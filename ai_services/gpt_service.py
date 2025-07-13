
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_gpt_response(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        temperature=0.7
    )
    return response.choices[0].message['content']


import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

async def get_gemini_response(question: str) -> str:
    response = model.generate_content(question)
    return response.text


from ai_services.gpt_service import get_gpt_response

async def get_copilot_response(question: str) -> str:
    system_prompt = "You are GitHub Copilot. Answer like a smart code assistant and explain everything in clean, commented code."
    return await get_gpt_response(f"{system_prompt}\n\n{question}")

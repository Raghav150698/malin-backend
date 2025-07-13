
from fastapi import FastAPI, Request
from pydantic import BaseModel
from ai_services.gpt_service import get_gpt_response
from ai_services.gemini_service import get_gemini_response
from ai_services.copilot_service import get_copilot_response
from ranking.ranker import rank_responses

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask-malin")
async def ask_malin(request: QuestionRequest):
    question = request.question

    gpt_response = await get_gpt_response(question)
    gemini_response = await get_gemini_response(question)
    copilot_response = await get_copilot_response(question)

    ranked = rank_responses([
        {"source": "GPT-4", "text": gpt_response},
        {"source": "Gemini", "text": gemini_response},
        {"source": "Copilot", "text": copilot_response},
    ])

    return {"best_answer": ranked[0], "all_answers": ranked}

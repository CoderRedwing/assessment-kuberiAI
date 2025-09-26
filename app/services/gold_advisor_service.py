from app.clients import gemini_client

async def get_advice(question: str) -> dict:
    response = await gemini_client.get_gemini_response(question)
    return response
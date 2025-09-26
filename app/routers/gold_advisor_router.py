from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services import gold_advisor_service

router = APIRouter(
    tags=["Gold Advisor"]   
)


class QuestionRequest(BaseModel):
    question: str

@router.post("/")
async def get_gold_advice(request: QuestionRequest):
    try:
        result = await gold_advisor_service.get_advice(question=request.question)

        if not result.get("success"):
            raise HTTPException(
                status_code=500,
                detail=result.get("message", "Failed to fetch AI response")
            )

        return {
            "success": True,
            "answer": result.get("answer")
        }

    except Exception as e:
        print(f"Error in gold_advisor_router: {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred."
        )
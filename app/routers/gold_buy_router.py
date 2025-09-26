from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlmodel import Session
from app.db.session import get_db

from app.services import gold_buy_service

router = APIRouter(
    tags=["Gold Purchase"] 
)


class GoldBuyRequest(BaseModel):
    user_id: int
    amount_in_inr: float = Field(ge=1, description="Minimum investment is ₹1")

@router.post("/buy")
async def buy_gold(request: GoldBuyRequest, db: Session = Depends(get_db)):

    try:
        result = await gold_buy_service.purchase_gold(
            db=db,
            user_id=request.user_id,
            amount_in_inr=request.amount_in_inr
        )

        if not result.get("success"):
            raise HTTPException(
                status_code=400,
                detail=result.get("message", "Could not complete the transaction.")
            )

        return result

    except Exception as e:
        print(f"Error in buy_gold router: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e) or "An internal server error occurred."
        )
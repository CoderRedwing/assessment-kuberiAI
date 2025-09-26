import os
import httpx
from sqlmodel import Session
from dotenv import load_dotenv
from app.models import gold_models

load_dotenv()

async def fetch_gold_price() -> float:
    url = "https://www.goldapi.io/api/XAU/INR"
    
    api_key = os.getenv("GOLD_API_KEY")
    if not api_key:
        raise ValueError("GOLD_API_KEY is not set in the .env file")
        
    headers = {"x-access-token": api_key}
    
    TROY_OUNCE_TO_GRAMS = 31.1035

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status() 
            data = response.json()

            price_inr_per_ounce = data.get("price")
            if price_inr_per_ounce is None:
                raise ValueError("Gold price (INR) not found in API response.")

            price_inr_per_gram = price_inr_per_ounce / TROY_OUNCE_TO_GRAMS

            return price_inr_per_gram

    except httpx.RequestError as e:
        print(f"HTTP Request Error fetching gold price: {e}")
        raise Exception("Unable to connect to the gold price API.")
    except Exception as e:
        print(f"Error processing gold price: {e}")
        raise Exception("Unable to fetch or process gold price.")


async def purchase_gold(db: Session, user_id: int, amount_in_inr: float) -> dict:
    try:
        price_per_gram = await fetch_gold_price()
        
        gold_in_grams = round(amount_in_inr / price_per_gram, 4)

        transaction_to_db = gold_models.GoldTransaction(
            user_id=user_id,
            amount_in_inr=amount_in_inr,
            gold_in_grams=gold_in_grams,
            price_per_gram=price_per_gram
        )
        
        db.add(transaction_to_db)
        db.commit()
        db.refresh(transaction_to_db)

        return {
            "success": True,
            "message": "Gold purchased successfully",
            "data": {
                "transactionId": transaction_to_db.id,
                "goldInGrams": transaction_to_db.gold_in_grams,
                "amountSpent": transaction_to_db.amount_in_inr,
                "pricePerGram": transaction_to_db.price_per_gram,
                "createdAt": transaction_to_db.created_at
            }
        }
    except Exception as e:
        print(f"Error in purchaseGold service: {e}")
        return {"success": False, "message": str(e)}
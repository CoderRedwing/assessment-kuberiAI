from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class GoldTransactionBase(SQLModel):
    user_id: int
    amount_in_inr: float
    gold_in_grams: float
    price_per_gram: float

class GoldTransactionCreate(GoldTransactionBase):
    pass

class GoldTransactionRead(GoldTransactionBase):
    id: int
    created_at: datetime
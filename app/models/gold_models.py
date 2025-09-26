from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class GoldTransaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True) 
    amount_in_inr: float
    gold_in_grams: float
    price_per_gram: float
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
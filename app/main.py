from fastapi import FastAPI
from app.routers import gold_advisor_router, gold_buy_router 

app = FastAPI(
    title="Gold Investment AI API",
    description="An API to provide AI-powered advice and handle gold transactions.",
    version="1.0.0"
)

app.include_router(
    gold_advisor_router.router,
    prefix="/api/gold-advisor"
)


app.include_router(
    gold_buy_router.router,
    prefix="/api/gold-purchase"
)


@app.get("/", tags=["Root"])
def read_root():
    return {"success": True, "message": "Gold Investment API is running "}
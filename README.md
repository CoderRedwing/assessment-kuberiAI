# Gold Investment AI API

A modern, asynchronous backend service built with FastAPI to provide AI-powered financial advice on gold investments and simulate gold purchase transactions using live market data.

---

## Features

### AI-Powered Advisor

- Uses Google Gemini API to provide professional advice on gold investment questions.

### Live Gold Pricing

- Integrates with GoldAPI.io to fetch real-time INR prices.

### Transaction Simulation

- Simulates gold purchases and calculates grams based on live price.

### Asynchronous & High Performance

- Fully async API endpoints and database calls for fast, concurrent performance.

### Database Integration

- SQLModel with PostgreSQL for persistent storage.

### Automatic API Documentation

- Interactive Swagger UI and ReDoc available out-of-the-box.

---

## Tech Stack

- Framework: FastAPI
- Database: PostgreSQL
- ORM: SQLModel (built on Pydantic and SQLAlchemy)
- AI Model: Google Gemini Pro
- External APIs: GoldAPI.io
- Server: Uvicorn (development), Gunicorn (production)
- Libraries: `httpx` for async API calls

---

## Project Setup and Installation

### Prerequisites

- Python 3.9+
- Running PostgreSQL database

### Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Copy the sample `.env` file and fill in your credentials:

```bash
cp .env.sample .env
```

```ini
DATABASE_URL="postgresql://user:password@host:port/dbname"
GEMINI_API_KEY="your_gemini_key"
GOLD_API_KEY="your_goldapi_key"
```

### Set Up the Database

```bash
python create_db.py
```

---

## Running the Application

### Development

```bash
uvicorn app.main:app --reload --port 8000
```

- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

| Method | Endpoint             | Description                              | Request Body                                      |
| ------ | -------------------- | ---------------------------------------- | ------------------------------------------------- |
| POST   | `/api/gold-advisor/` | Get AI-powered advice on gold investment | `{"question": "Is now a good time to buy gold?"}` |
| POST   | `/api/gold-purchase` | Simulate a gold purchase transaction     | `{"user_id": 123, "amount_in_inr": 10}`           |
| GET    | `/`                  | Check if the API is running              | N/A                                               |

---

### Example Requests and Responses

**Gold Advisor Example**

```bash
curl -X POST "http://127.0.0.1:8000/api/gold-advisor/" \
-H "Content-Type: application/json" \
-d '{"question": "Is now a good time to buy gold?"}'
```

**Sample Response**

```json
{
  "success": true,
  "answer": "Gold is a stable investment option. Start small, diversify, and explore digital gold via our app today."
}
```

**Gold Purchase Example**

```bash
curl -X POST "http://127.0.0.1:8000/api/gold-purchase" \
-H "Content-Type: application/json" \
-d '{"user_id":123,"amount_in_inr":10}'
```

**Sample Response**

```json
{
  "success": true,
  "message": "Gold purchased successfully",
  "data": {
    "transactionId": 3,
    "goldInGrams": 0.0009,
    "amountSpent": 10.0,
    "pricePerGram": 10684.070924494,
    "createdAt": "2025-09-26T05:10:16.413038"
  }
}
```

---

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn app.main:app --reload --port 8000`
3. Open Swagger Docs and test your first request.

---

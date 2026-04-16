# DCF Valuation Web App

A production-oriented Discounted Cash Flow valuation application built with FastAPI, PostgreSQL, and SQLAlchemy.

## Features

- `POST /calculate-dcf` REST API
- Validates inputs with Pydantic
- Stores every calculation in PostgreSQL
- Returns yearly cash flows, discounted cash flows, and valuation
- Includes optional terminal value calculation
- Simple frontend UI with HTML and JavaScript

## Files

- `main.py` — FastAPI application and routes
- `database.py` — PostgreSQL connection and session management
- `models.py` — SQLAlchemy database models
- `schemas.py` — Pydantic request/response models
- `dcf.py` — DCF calculation logic
- `static/index.html` — frontend form and client-side logic
- `requirements.txt` — Python dependencies

## Additional features

- `GET /history` endpoint returns the latest calculations
- Frontend includes a recent calculations history table

## Setup

1. Create a PostgreSQL database:

```bash
createdb dcf_db
```

2. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configure the database connection.

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

4. Run the app:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5. Open the frontend in your browser:

- http://localhost:8000/
- Swagger docs: http://localhost:8000/docs
- History API: http://localhost:8000/history

## Notes

- The app uses `DATABASE_URL` from environment variables.
- If `discount_rate` is higher than `growth_rate`, a terminal value is included.
- Stored valuation is the final valuation after discounting cash flows, and includes terminal value when available.

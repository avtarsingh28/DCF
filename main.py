from pathlib import Path
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import dcf
import models
import schemas
from database import get_db, init_db

app = FastAPI(
    title="DCF Valuation API",
    description="A production-ready FastAPI app for discounted cash flow valuation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = Path(__file__).resolve().parent / "static"

init_db()


@app.get("/", response_class=FileResponse)
def read_home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/calculate-dcf", response_model=schemas.DCFOutput)
def calculate_dcf_endpoint(
    payload: schemas.DCFInput, db: Session = Depends(get_db)
) -> schemas.DCFOutput:
    try:
        result = dcf.calculate_dcf(
            revenue=payload.revenue,
            growth_rate=payload.growth_rate,
            discount_rate=payload.discount_rate,
            years=payload.years,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    valuation = (
        result["total_valuation_with_terminal"]
        if result["total_valuation_with_terminal"] is not None
        else result["final_valuation"]
    )

    db_entry = models.DCFResult(
        revenue=payload.revenue,
        growth_rate=payload.growth_rate,
        discount_rate=payload.discount_rate,
        years=payload.years,
        valuation=valuation,
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    return schemas.DCFOutput(**result)


@app.get("/history", response_model=List[schemas.DCFHistoryItem])
def read_history(db: Session = Depends(get_db)) -> List[schemas.DCFHistoryItem]:
    records = (
        db.query(models.DCFResult)
        .order_by(models.DCFResult.created_at.desc())
        .limit(10)
        .all()
    )
    return records

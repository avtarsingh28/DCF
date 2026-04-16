from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, confloat, PositiveInt


class DCFInput(BaseModel):
    revenue: confloat(gt=0)
    growth_rate: confloat(ge=0)
    discount_rate: confloat(gt=0)
    years: PositiveInt

    class Config:
        schema_extra = {
            "example": {
                "revenue": 1000000.0,
                "growth_rate": 0.1,
                "discount_rate": 0.12,
                "years": 5,
            }
        }


class YearlyCashFlow(BaseModel):
    year: int
    projected_cash_flow: float
    discounted_cash_flow: float


class DCFOutput(BaseModel):
    yearly_cash_flows: List[YearlyCashFlow]
    final_valuation: float
    terminal_value: Optional[float] = None
    discounted_terminal_value: Optional[float] = None
    total_valuation_with_terminal: Optional[float] = None


class DCFHistoryItem(BaseModel):
    id: int
    revenue: float
    growth_rate: float
    discount_rate: float
    years: int
    valuation: float
    created_at: datetime

    class Config:
        orm_mode = True

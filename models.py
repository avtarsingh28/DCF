from sqlalchemy import Column, DateTime, Float, Integer
from sqlalchemy.sql import func
from database import Base


class DCFResult(Base):
    __tablename__ = "dcf_results"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float, nullable=False)
    growth_rate = Column(Float, nullable=False)
    discount_rate = Column(Float, nullable=False)
    years = Column(Integer, nullable=False)
    valuation = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

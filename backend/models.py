from typing import Optional
from datetime import date, datetime, timezone
from sqlmodel import SQLModel, Field

class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[float] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TripRequest(SQLModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[float] = None

class Stop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    sort_order: int
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    cost: Optional[float] = None
    time_zone: Optional[str] = None
    arrival_time: Optional[datetime] = None
    departure_time: Optional[datetime] = None

class StopRequest(SQLModel):
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    cost: Optional[float] = None
    time_zone: Optional[str] = None
    arrival_time: Optional[datetime] = None
    departure_time: Optional[datetime] = None

class StopReorder(SQLModel):
    ids: list[int]
from pydantic import BaseModel, Field
from typing import Optional

class LocationUpdate(BaseModel):
    person_id: int = Field(..., description="Unique identifier for the person")
    latitude: float = Field(..., ge=-90, le=90, description="Latitude of the current location")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude of the current location")
    timestamp: Optional[str] = Field(None, description="ISO8601 timestamp of the update")
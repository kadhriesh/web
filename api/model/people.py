from pydantic import BaseModel, Field
from typing import Optional

class People(BaseModel):
    id: int = Field(..., description="Unique identifier for the person")
    first_name: str = Field(..., description="First name of the person")
    last_name: str = Field(..., description="Last name of the person")
    email: Optional[str] = Field(None, description="Email address of the person")
    phone: Optional[str] = Field(None, description="Phone number of the person")
    age: Optional[int] = Field(None, ge=0, description="Age of the person")
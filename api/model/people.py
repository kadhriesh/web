from datetime import (
    datetime,
)
from typing import (
    Optional,
)

from pydantic import (
    BaseModel,
    Field,
)


class People(BaseModel):
    id: int = Field(..., description="Unique identifier for the person")
    first_name: str = Field(..., description="First name of the person")
    last_name: str = Field(..., description="Last name of the person")
    email: str = Field(..., description="Email address of the person")
    tag_id: Optional[str] = Field(None, description="Tag ID associated with the person")
    phone: Optional[str] = Field(None, description="Phone number of the person")
    dob: Optional[datetime] = Field(None, description="Age of the person")
    created_at: Optional[datetime] = Field(
        None, description="Timestamp when the person was created"
    )
    updated_at: Optional[datetime] = Field(
        None, description="Timestamp when the person was last updated"
    )

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


class RafidTag(BaseModel):
    tag_id: str = Field(..., description="Unique identifier for the tag")
    tag_name: str = Field(..., description="Name of the tag")
    created_at: Optional[datetime] = Field(..., description="Timestamp when the tag was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when the tag was last updated")
    status: str = Field(..., description="Current status of the tag")
    associated_with: Optional[str] = Field(None, description="Entity the tag is associated with")
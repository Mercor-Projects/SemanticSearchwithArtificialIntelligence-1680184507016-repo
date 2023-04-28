from typing import List, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from .base import PyObjectId


class Question(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    index_id: int = Field(...)
    text: str = Field(...)
    owner: Optional[str] = None
    embedding: List[float] = Field(..., min_items=512)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

from pydantic import BaseModel, Field
from typing import Optional
from .category import CategoryResponse

class QuestionCreate(BaseModel):

    text: str = Field(..., min_length=12, description="The content of the question")
    category_id: int = Field(..., description="ID of the assigned category")

class QuestionResponse(BaseModel):

    id: int
    text: str
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True

class MessageResponse(BaseModel):

    message: str
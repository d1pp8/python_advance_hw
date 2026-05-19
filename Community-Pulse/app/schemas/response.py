from pydantic import BaseModel, Field

class ResponseCreate(BaseModel):

    question_id: int = Field(..., description="The ID of the question being answered")
    is_agree: bool = Field(..., description="User's agreement or disagreement with the question")

class StatisticResponse(BaseModel):

    question_id: int
    agree_count: int
    disagree_count: int
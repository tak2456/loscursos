from pydantic import BaseModel, Field

class TodoSchema(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=5, max_length=100)
    priority: int = Field(gt=0, lte=5)
    complete: bool = False

    # class Config:
    #     orm_mode = True
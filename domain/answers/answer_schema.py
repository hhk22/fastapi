from pydantic import BaseModel
from pydantic.functional_validators import field_validator


class AnswerCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('The value is empty')
        return v

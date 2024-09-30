from typing import Optional
from pydantic import BaseModel

class Question(BaseModel):
    content: str

class Answer(BaseModel):
    content: str
    url: Optional[str]
    page: Optional[str]

class SearchResponse(BaseModel):
    doc_id: Optional[str]
    title: Optional[str]
    url: Optional[str]
    body_content: Optional[str]
    page: Optional[str]
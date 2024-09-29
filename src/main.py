
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Answer(BaseModel):
    content: str

@app.post("/seek")
async def seek(query: str) -> Answer:
    return Answer(content=f'Answer to "{query}"')



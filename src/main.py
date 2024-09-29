
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    content: str

@app.post("/seek")
async def seek(question: Message) -> Message:
    return Message(content=f'Answer to "{question.content}"')



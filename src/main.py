from dotenv import load_dotenv
load_dotenv(override=True)

from fastapi import FastAPI
from models import Question, Answer
from query import query

app = FastAPI()

@app.post("/seek")
async def seek(question: Question) -> Answer:
    return query(question.content)



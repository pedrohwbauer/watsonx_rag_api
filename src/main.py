
from fastapi import FastAPI

app = FastAPI()


@app.get("/seek")
def read_root():
    return {"content": "aaaaaaaaaaaaaaaaa"}



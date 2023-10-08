from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn main:app --reload

class perfume(BaseModel):
    title: str
    description: str
    thumnailUrl: str

@app.get("/")
async def hello(name: str):
    return {"messages" : perfume(title = "perfume name", description = "this perfume is.." ,thumnailUrl = "url")}
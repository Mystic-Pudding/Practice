from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DataInput(BaseModel):
    name: str
    ratio: float
    size: int

class PredictOutput(BaseModel):
    prob: float
    prediction: int

@app.post("/pydantic", response_model=PredictOutput)
def pydanticPost(dataRequest: DataInput):
    print(dataRequest)
    return {"prob" : 0.1, "prediction" : 0}

@app.get("/{name}")
async def root(name: str):
    return {"message" : "hello"}

@app.get("/home/{name}")
async def home(name: int):
    return {"message" : "home"}

@app.post("/")
def rootPost(msg: str):
    return {"Hello" : "Post", "msg": msg}
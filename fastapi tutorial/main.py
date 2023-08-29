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

@app.get("/home/{name}")    # url/home/hello    or      url/home/hello?age=20
async def home(name: str, age: int):    
    return {"message" : name, "age" : age}

@app.post("/")
def rootPost(msg: str):
    return {"Hello" : "Post", "msg": msg}
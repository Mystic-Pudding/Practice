from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel

# uvicorn fromYoutube:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return {"Message" : "hello world"}

@app.post("/")
async def post():
    return {"message" : "hello from the post route"}

@app.get("/items")
async def items():
    return {"messages" : "items route"}

@app.get("/items/{itemId}")
async def getItem(itemId: int):
    return {"itemID" : itemId}

class Food(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{foodName}")
async def getFood(foodName: Food):
    if foodName == Food.fruits:
        return {"foodName" : foodName}
    if foodName.value == "vegetables":
        return {"foodName" : foodName}
    
#http://127.0.0.1:8000/users?name=mystic&age=6 get부분에 포함되어 있지 않은 변수는 optinal로 ?뒤에 작성.
@app.get("/users")
async def users(name: str, age: int = 10):
    return {"name" : name, "age" : age}

@app.get("/users/{userName}")
async def getUser(userName: str, height: Optional[float] = None):
    if height:
        return {"userName" : userName, "height" : height}
    else:
        return {"userName" : userName}
    
class SubItem(BaseModel):
    name: str
    price: float

class Item(BaseModel):
    name: str 
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    sub: SubItem

class LimitDate(BaseModel):
    Open: str 
    Close: str

@app.post("/items")
async def createItem(item: Item, limit: LimitDate):
    return {"receivedItem" : item, "receivedLimit" : limit}
    
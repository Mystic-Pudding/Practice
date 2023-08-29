from fastapi import APIRouter

ncf = APIRouter(prefix='/ncf')

@ncf.get('/')
async def startNcf():
    return {"msg" : "NCF"}

@ncf.get('/model')
async def ncfModel():
    return {'msg' : 'ncf model'}

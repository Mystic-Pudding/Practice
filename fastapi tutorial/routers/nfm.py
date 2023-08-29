from fastapi import APIRouter

nfm = APIRouter(prefix='/nfm')

@nfm.get('/')
async def startNfm():
    return {"msg" : "NFM"}

@nfm.get('/model')
async def ncfModel():
    return {'msg' : 'nfm model'}

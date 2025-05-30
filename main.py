from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
@app.get("/")
async def welcome():
    try:
        return {"message":"Hello from RCW1003"}
    except Exception as e:
        print (f'Exception: {e}')
        raise HTTPExceptio(status_code=500 , detail=str(e))
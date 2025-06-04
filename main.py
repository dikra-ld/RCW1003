from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello from RCW1003"}

@app.get("/test")
async def test():
    return {"message": "Hello from /test endpoint!"}

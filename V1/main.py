from fastapi import FastAPI
from routers.user import user_router

app=FastAPI(
    title="Grubbies API",
    version="1.0"
)

app.include_router(user_router, prefix= "/v1", tags=["User"])
@app.get("/")
async def home():
    return {"message": "Welcome to Grubbies!"}
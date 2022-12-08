from fastapi import FastAPI

from app.server.routes.client import router as ClientRouter

app = FastAPI()

app.include_router(ClientRouter, tags=["Client"], prefix="/client")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

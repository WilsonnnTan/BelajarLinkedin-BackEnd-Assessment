import os
import asyncio
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api import auth, classes, enrollment

app = FastAPI()
security = HTTPBearer()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(classes.router, prefix="/class", tags=["class"])
app.include_router(enrollment.router, prefix="/enroll", tags=["enrollment"])

async def main():
    config = uvicorn.Config("app:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
   asyncio.run(main())

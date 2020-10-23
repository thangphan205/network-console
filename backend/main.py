import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from settings import settings
from models import models
from db.database import engine

from logger import init_logging

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="network_console_api", openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(api_router, prefix=settings.API_V1_STR)
# init_logging()


origins = [
    "http://console.hocmang.net",
    "https://console.hocmang.net",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)

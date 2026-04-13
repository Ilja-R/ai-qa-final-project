from fastapi import FastAPI
from app.routes.pipeline import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="QA Pipeline System")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] etc
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
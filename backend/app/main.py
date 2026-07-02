from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.chat import router

app = FastAPI(
    title="Enterprise AI Telecom Assistant",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include chat router
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise AI Telecom Assistant"
    }
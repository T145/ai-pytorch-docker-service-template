from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from torch import cuda

app = FastAPI()
server_host = "http://localhost:8000"
origins = ["*", server_host]
device = "cuda" if cuda.is_available() else "cpu"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"device": device}


@app.get("/health")
async def health_check():
    return {"status": "ok"}

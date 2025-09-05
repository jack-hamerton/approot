from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, community, safeguards

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(community.router, prefix="/community", tags=["community"])
app.include_router(safeguards.router, prefix="/safeguards", tags=["safeguards"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
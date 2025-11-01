from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ArthaShield Explainability Engine MVP")
app.include_router(router)

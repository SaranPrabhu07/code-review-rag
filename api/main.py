from fastapi import FastAPI
from api.routes.review import router as review_router

app = FastAPI(title="Code Review RAG")

app.include_router(review_router)

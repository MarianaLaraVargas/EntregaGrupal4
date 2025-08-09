from fastapi import FastAPI
from routes import inventory, pipeline

app = FastAPI()

app.include_router(inventory.router)
app.include_router(pipeline.router)

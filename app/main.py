from fastapi import FastAPI

from database import Base, engine

# Import models BEFORE create_all()
import models

from routers import company, job

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(company.router)
app.include_router(job.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
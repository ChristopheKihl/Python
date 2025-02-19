from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    return "test"

@app.get("/")
async def root():
    return "home"
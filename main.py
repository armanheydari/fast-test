from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Marketing(BaseModel):
    campaign_name: str
    finance: int
    conversion_rate: float


@app.get("/")
async def root():
    return {"Arman": "Welcome to application"}


@app.get("/marketing_data")
async def marketing():
    response = Marketing(
        campaign_name="Mozhaaawwn",
        finance=26,
        conversion_rate=1.2
    )
    return response


@app.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

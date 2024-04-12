from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/time")
def get_time() -> dict[str, int]:
    local_time = time.localtime() 
    return {"hours": local_time.tm_hour, "minutes": local_time.tm_min, "seconds": local_time.tm_sec}
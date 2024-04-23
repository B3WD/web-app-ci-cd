from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time


app = FastAPI()


html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World!</title>
</head>
<body>
    <h1>Hello World</h1>
    <button type="button">Hello world!</button>
</body>
</html>
"""

@app.get("/")
async def root():
  return HTMLResponse(content=html_content, media_type="text/html")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/time")
def get_time() -> dict[str, int]:
    local_time = time.localtime() 
    return {"hours": local_time.tm_hour, "minutes": local_time.tm_min, "seconds": local_time.tm_sec}

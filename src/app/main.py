import uvicorn
from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"For real"}

# @app.post("/createposts")
# def create_posts(payload: dict = Body()):
#     return {"message": "successfully created post foo"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)
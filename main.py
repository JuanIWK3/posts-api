from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

posts = []

@app.get("/")
def root():
    return {"message": "Hello eitititipi"}

@app.get("/posts")
def get_posts():
    return posts 

@app.post("/create")
def create_posts(payload: dict = Body(...)):
    posts.append({
        "id": len(posts) + 1,
        "title": payload["title"],
        "content": payload["content"]
    })
    return {
        "status": "created",
        "post": {
            "id": len(posts),
            "title": payload["title"],
            "content": payload["content"]
        }
    }

from fastapi import FastAPI

app = FastAPI(title="StoryForge Transparent Pipeline")

@app.get("/")
def root():
    return {"message": "Welcome to the Transparent Pipeline"}

from fastapi import FastAPI

app = FastAPI(title="StoryForge Transparent Pipeline")

@app.get("/")
def root():
    return {"message": "Welcome to the Transparent Pipeline"}

@app.get("/ui")
def serve_ui():
    from fastapi.responses import HTMLResponse
    from pathlib import Path
    html_file = Path(__file__).parent / "ui.html"
    return HTMLResponse(content=html_file.read_text())

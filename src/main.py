import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="FaceApp-API", version="v0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)


app.mount('/img', StaticFiles(directory="src/img"), name="img")


@app.get("/", response_class=RedirectResponse, status_code=308)
async def index(request: Request):
    return "./docs"

if __name__ == "__main__":
    uvicorn.run("src.main:app")

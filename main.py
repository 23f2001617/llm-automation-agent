from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Automation Agent API is running!"}

@app.post("/run")
async def run_task(task: str):
    if not task:
        raise HTTPException(status_code=400, detail="Task description is required")
    return {"message": f"Executing task: {task}"}

@app.get("/read")
async def read_file(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r") as f:
        content = f.read()
    return {"content": content}


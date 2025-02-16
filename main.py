import openai
import os
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Secure API Key Handling
openai_client = openai.OpenAI(
    api_key=os.environ.get("AIPROXY_TOKEN", ""),  # Avoid hardcoding keys
    base_url="https://aiproxy.sanand.workers.dev/v1"
)

print("OpenAI client initialized.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_email_from_text(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

@app.get("/")
def read_root():
    return {"message": "Automation Agent API is running!"}

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_task(request: TaskRequest):
    task = request.task.lower()

    try:
        if "extract the sender’s email" in task:
            email_file = os.path.join(BASE_DIR, "data", "email.txt")
            output_file = os.path.join(BASE_DIR, "data", "email-sender.txt")

            if not os.path.exists(email_file):
                raise HTTPException(status_code=404, detail="email.txt not found.")

            with open(email_file, "r") as file:
                email_text = file.read()

            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Extract the sender’s email from the given text."},
                    {"role": "user", "content": email_text}
                ]
            )

            extracted_email = getattr(response.choices[0].message, "content", "").strip()

            if not extracted_email:
                raise HTTPException(status_code=500, detail="LLM did not return a valid email.")

            with open(output_file, "w") as file:
                file.write(extracted_email)

            return {"message": "Email extracted successfully.", "email": extracted_email}

        else:
            raise HTTPException(status_code=400, detail="Task not recognized.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

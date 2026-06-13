from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Document Chat API is running"}
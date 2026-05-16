from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def checkHealth():
    return {
        "message" : "Fastapi is working before merge"
    }



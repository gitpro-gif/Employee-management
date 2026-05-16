from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def checkHealth():
    return {
        "message" : "Fastapi is working before merge"
    }
    
@app.get("/getallstudents")
def getallStudents():
    return {
        "message" : students
    }
    



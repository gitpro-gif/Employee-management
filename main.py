from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def checkHealth():
    return {
        "message" : "Fastapi is working before merge"
    }

@app.post("/addstudent")
def CreateEmployee(id: int, name: str, department: str):
    student = {
        "id": id,
        "name": name,
        "department": department
    }
    
    students.append(student)
    return {
        "message" : "Student added successfully",
        "data": student
    }


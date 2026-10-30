from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float = Field(ge=0, le=100)

students = []

@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return student

@app.get("/students")
def get_students():
    return students

@app.get("/students")
def get_students(course: str = None):
    if course:
        filtered_students = []
        for s in students:
            if s.course == course:
                filtered_students.append(s)
        return filtered_students
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for s in students:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for i in range(len(students)):
        if students[i].id == id:
            students[i] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{id}")
def delete_student(id: int):
    for i in range(len(students)):
        if students[i].id == id:
            del students[i]
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")

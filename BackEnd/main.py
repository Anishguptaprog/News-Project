from fastapi import FastAPI, Path
# from requests import delete
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "anish",
        "age": 20,
        "class": "3rd yr"
    },
    2: {
        "name": "ani",
        "age": 2,
        "class": "3rd",
    },
    3: {
        "name": "a",
        "age": 200,
        "class": "3"
    }
}


class stu(BaseModel):
    name: str
    age: int
    year: str


class updatestu(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/about")
def about():
    return {"Data": "Student record page"}


@app.get("/get-student/{student_id}")
def get_stu(student_id: int = Path(None, description="ID of the student you want to know", gt=0)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_stu(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: stu):
    if student_id in students:
        return {"Error": "Student exits"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_stu(student_id: int, student: updatestu):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        student[student_id].name = student.name

    if student.age != None:
        student[student_id].age = student.age

    if student.year != None:
        student[student_id].year = student.year

    students[student_id] = student
    return students[student_id]

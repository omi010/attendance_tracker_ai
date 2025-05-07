from fastapi import APIRouter
from app import models, schemas

router = APIRouter()

@router.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    return db_student

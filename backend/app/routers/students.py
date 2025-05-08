from fastapi import APIRouter
# Use relative imports instead of absolute
from .. import models, schemas

router = APIRouter()

@router.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    return db_student

from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    class_name: str
    roll_no: int
    contact: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

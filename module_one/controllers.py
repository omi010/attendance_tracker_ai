from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
import random  # Placeholder for AI prediction logic

# Initialize the router
router = APIRouter()

# Simulated database (replace with actual DB like Firebase)
attendance_db = [
    {"student_id": 1, "name": "John Doe", "attendance_date": "2025-05-08", "status": "Present"},
    {"student_id": 2, "name": "Jane Smith", "attendance_date": "2025-05-08", "status": "Absent"},
]

# Pydantic models
class AttendanceRecord(BaseModel):
    student_id: int
    name: str
    attendance_date: datetime
    status: str

class AbsenteePredictionRequest(BaseModel):
    student_id: int
    name: str
    last_attendance_date: datetime

# Fetch all attendance records
@router.get("/attendance/", response_model=List[AttendanceRecord])
async def get_attendance():
    return attendance_db

# Fetch a specific student's attendance
@router.get("/attendance/{student_id}", response_model=AttendanceRecord)
async def get_student_attendance(student_id: int):
    for record in attendance_db:
        if record["student_id"] == student_id:
            return record
    raise HTTPException(status_code=404, detail="Student attendance not found")

# Mark attendance
@router.post("/attendance/", response_model=AttendanceRecord)
async def mark_attendance(attendance: AttendanceRecord):
    attendance_db.append(attendance.dict())
    return attendance

# Update attendance status (Present/Absent)
@router.put("/attendance/{student_id}", response_model=AttendanceRecord)
async def update_attendance_status(student_id: int, status: str):
    for record in attendance_db:
        if record["student_id"] == student_id:
            record["status"] = status
            return record
    raise HTTPException(status_code=404, detail="Student attendance not found")

# Delete a student's attendance record
@router.delete("/attendance/{student_id}", status_code=204)
async def delete_attendance(student_id: int):
    global attendance_db
    attendance_db = [record for record in attendance_db if record["student_id"] != student_id]
    return

# AI absentee prediction (mock logic)
@router.post("/attendance/predict-absent", response_model=dict)
async def predict_absenteeism(request: AbsenteePredictionRequest):
    prediction = random.choice(["Present", "Absent"])  # Replace with real ML model
    return {
        "student_id": request.student_id,
        "name": request.name,
        "predicted_status": prediction
    }

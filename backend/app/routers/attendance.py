from fastapi import APIRouter

router = APIRouter()

@router.post("/attendance/")
def mark_attendance(attendance_data: dict):
    return {"status": "Attendance marked successfully"}

from fastapi import APIRouter

router = APIRouter()

@router.get("/reports/{student_id}")
def get_reports(student_id: int):
    return {"status": "Report generated", "student_id": student_id}

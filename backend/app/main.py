from fastapi import FastAPI
from app.routers import students, attendance, reports, notifications, auth_routes, ocr

app = FastAPI()

app.include_router(students.router)
app.include_router(attendance.router)
app.include_router(reports.router)
app.include_router(notifications.router)
app.include_router(auth_routes.router)
app.include_router(ocr.router)

from fastapi import FastAPI
# Use relative imports since we're inside the app package
from .routers import students, attendance, reports, notifications, auth_routes, ocr

# For module_one, use a direct import since it's in the project root
import sys
import os
# Add project root to path to allow importing module_one
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from module_one.controllers import router as module_one_router

app = FastAPI()

app.include_router(students.router)
app.include_router(attendance.router)
app.include_router(reports.router)
app.include_router(notifications.router)
app.include_router(auth_routes.router)
app.include_router(ocr.router)
app.include_router(module_one_router)

# If this file is run directly, start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)

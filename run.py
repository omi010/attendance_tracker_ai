"""
Startup script for the attendance tracker application.
Run this script from the project root to start the FastAPI server.
"""
import uvicorn

if __name__ == "__main__":
    # Start the FastAPI application
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)

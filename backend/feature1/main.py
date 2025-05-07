import os
import sys
from pathlib import Path

# Absolute path configuration - MUST BE FIRST
current_dir = Path(__file__).parent
backend_dir = current_dir.parent.parent  # Goes to Bagan_bilash/backend
sys.path.insert(0, str(backend_dir))

# Core imports
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, Response
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

# Local imports (using explicit relative imports)
from . import models
from . import schemas
from .database import SessionLocal, engine

# Initialize app
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Configure paths
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "frontend/static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "frontend/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ... (keep all your existing route handlers unchanged)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Different port for testing
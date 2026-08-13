import shutil
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import FileResponse
from backend.main import create_folder_structure,display
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/generate_folders")
async def generate_folder_structure(file:UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    zip_path = create_folder_structure(file_path)
    return FileResponse(path = zip_path,
                        filename="folder_structure.zip",
                        media_type="application/zip")


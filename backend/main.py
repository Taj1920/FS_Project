import zipfile
from uuid import uuid4
from backend.services.file_reader import convert_dataframe
from backend.services.tree_builder import build_tree
from backend.services.default_folders import add_default_folders
from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)
ROOT = Path(__file__).resolve().parents[1]



def display(node,level=0):
    print(("|- "*level)+ node.name)
    for child in node.children.values():
        display(child,level+1)

def create_folders(node,parent_path):
    current_path = parent_path / node.name
    current_path.mkdir(parents=True,exist_ok=True)

    if node.name=="tutorials":
        (current_path / "tutorials.md").touch(exist_ok=True)
        (current_path / "tutorials.pdf").touch(exist_ok=True)
    elif node.name=="docs":
        (current_path / "images").mkdir(exist_ok=True)
        (current_path / "slides").mkdir(exist_ok=True)
        (current_path / "notes.pdf").touch(exist_ok=True)
        (current_path / "notes.md").touch(exist_ok=True)
        (current_path / "documents.docx").touch(exist_ok=True)
        (current_path / "data.xlsx").touch(exist_ok=True)
    elif node.name=="playground":
        (current_path / "sample.txt").touch(exist_ok=True)

    for child in node.children.values():
        create_folders(child,current_path)

def zip_folder(folder_path,zip_path):
    folder_path = Path(folder_path)
    zip_path = Path(zip_path)
    with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as zipf:
        for file in folder_path.rglob("*"):
            zipf.write(file,arcname=file.relative_to(folder_path))
    logger.info("zip folder created")
    return zip_path

def create_folder_structure(file_path):
    df = convert_dataframe(file_path)
    subject = df[df.columns[0]].unique()[0]
    logger.info(f"Folder creation initiated for {subject}")
    root = build_tree(df)
    logger.info("adding default folders...")
    add_default_folders(root)
    logger.info("default folders added...")
    job_id = uuid4().hex
    output_path = ROOT / "output" / job_id
    logger.info(f"Folder creation for {job_id} initiated...")
    create_folders(root, output_path)
    logger.info("Folder creation finished")
    zipfile = zip_folder(output_path,ROOT / f"folder_structure{job_id}.zip")
    logger.info(f"folder structure for {subject} created successfully")
    return zipfile


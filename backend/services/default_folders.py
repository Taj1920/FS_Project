from backend.services.tree_builder import FolderNode
from utils.logger import get_logger

logger = get_logger(__name__)
def add_default_folders(node):
    
    if node.level>=0:
        is_leaf = len(node.children)==0
        #tutorials and docs for every level
        node.add_child(FolderNode("tutorials",-1))
        node.add_child(FolderNode("docs",-1))

        if is_leaf and node.level>=4:
            node.add_child(FolderNode("video",-1))
        if node.level>=3:
            node.add_child(FolderNode("playground",-1))
    for child in node.children.values():
        if child.name not in ["tutorials","docs","playground","video"]:
            add_default_folders(child)
    
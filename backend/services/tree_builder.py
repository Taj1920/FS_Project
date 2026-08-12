import re
import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)
class FolderNode:
    def __init__(self,name,level,parent=None):
        self.name = name
        self.level = level
        self.parent = parent
        self.children = {}
    
    def add_child(self,child):
        if child.name not in self.children:
            child.parent = self
            self.children[child.name] = child
        return self.children[child.name]
def clean_folder_names(folder_name):
    folder = str(folder_name)
    folder = folder.strip()
    folder = re.sub(r'[<>:"/\\|?*]',"",folder)
    return folder

def build_tree(df):
    logger.info("Building Folder tree...")
    if df is not None:
            root = FolderNode("ELP",-1)
            logger.info("Ignoring empty cells..")
            logger.info("folder name cleaning initiated..")
            for _,row in df.iterrows():
                current=root
                for level,folder_name in enumerate(row):
                    if pd.isna(folder_name):
                        continue
                    folder_name = clean_folder_names(folder_name)
                    child = FolderNode(folder_name,level)
                    current = current.add_child(child)
            logger.info("folder name cleaning finished..")
            logger.info("Folder tree build completed...")
            return root

        
# python = FolderNode("Python")
# basics = FolderNode("Basics")
# oops = FolderNode("Oops")
# variables = FolderNode("variables")
# datatypes = FolderNode("datatypes")
# inheritance = FolderNode("inheritance")
# polymorphism = FolderNode("polymorphism")

# python.add_child(basics)
# python.add_child(basics)

# basics.add_child(variables)
# basics.add_child(datatypes)


# python.add_child(oops)
# oops.add_child(inheritance)
# oops.add_child(polymorphism)




import pandas as pd
import os
from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)


def convert_dataframe(file_path):
        try:
            logger.info("converting into dataframe....")
            if os.path.exists(file_path):
                if str(file_path).endswith(".csv"):
                    df = pd.read_csv(file_path,index_col=0,skip_blank_lines=True)
                elif str(file_path).endswith(".xls") or str(file_path).endswith(".xlsx"):
                    df = pd.read_excel(file_path,index_col=0)
                else:
                    logger.warning("file is not .csv or .xlsx")
                drop_cols = [col for col in df.columns if col.startswith("Unnamed")]
                if drop_cols!=[]:
                    df = df.drop(drop_cols,axis=1)
                df.reset_index(inplace=True)
                logger.info("Data frame created")
                logger.info(f"sample dataframe: {df.head(3)}")
                logger.info(f"dataframe info: {df.info()}")
                return df
            else:
                logger.warning(f"Data file does not exist")
        except Exception as error:
            logger.error(f"Dataframe creation failed: {error}")
            return None

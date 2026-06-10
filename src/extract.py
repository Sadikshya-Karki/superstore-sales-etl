import pandas as pd
from src.logger import setup_logger

logging = setup_logger()

def extract_data(file_path):

    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    logging.info(f"Data extracted successfully. Shape: {df.shape}")

    return df
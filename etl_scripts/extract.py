from typing import List
import pandas as pd

def extract_data(file_path: str, columns: List[dict]) -> pd.DataFrame:
    # get columns name list
    column_name_list = [item['name'] for item in columns]
    return pd.read_csv(file_path, names=column_name_list)
    
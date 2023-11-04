from typing import List
import pandas as pd

def transform_data(dataset: pd.DataFrame, columns: List[dict]) -> pd.DataFrame:
    # columns with type numeric
    float_column_list = [item['name'] for item in columns if item['type'] == 'numeric']
    # convert data types of numeric columns
    dataset[float_column_list] = dataset[float_column_list].apply(pd.to_numeric, errors='coerce')
    # drop rows with missing values or errors values
    dataset.dropna(inplace=True)
    return dataset


def summarize_statistics(dataset: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return dataset[columns].describe()
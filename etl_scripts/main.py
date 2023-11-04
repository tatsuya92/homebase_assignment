import json
import extract
import transform
import load
from decouple import config
from typing import Dict
from logs.etl_log import ETLLogger

etl_logger = ETLLogger(streaming=True)

def load_configuration() -> Dict[str, any]:
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)
        return config

def load_connection_params() -> Dict[str, any]:
    # get postgresql params
    return {
        'host': config('DB_POSTGRE_HOST'),
        'port': config('DB_POSTGRE_PORT',cast=int),
        'username': config('DB_POSTGRE_USERNAME'),
        'password': config('DB_POSTGRE_PASSWORD'),
        'database': config('DB_POSTGRE_DATABASE')
    }

def execute_etl_data():
    try:
        # load the configuration
        config = load_configuration()
        # source data information
        source_data = config.get('source_data', {})
        source_file_path = source_data.get('file_path')
        source_columns = source_data.get('columns')
        summary_columns = source_data.get('summary_columns')
        schema = source_data.get('schema')
        table_name = source_data.get('table_name')
        # validate source data
        if not source_file_path or not source_columns or not summary_columns or not schema or not table_name:
            etl_logger.error("[DATA][ETL] lack source configuration")
        # load posgresql connection params
        connection_params = load_connection_params()
        # extact data 
        dataset = extract.extract_data(source_file_path, source_columns)
        etl_logger.info("[DATA][ETL] extract data: done")
        # transform data
        dataset = transform.transform_data(dataset, source_columns)
        etl_logger.info("[DATA][ETL] transform data: done")
        # summarize statistics
        summarize_data = transform.summarize_statistics(dataset, summary_columns)
        etl_logger.info(f"[DATA][ETL] summary statistics result: {summarize_data}")
        # load data
        load.load_data(dataset, connection_params, table_name, schema, etl_logger)
    except Exception as ex:
        etl_logger.error(f"[DATA][ETL] fail ETL data: {str(ex)}")


if __name__ == "__main__":
    execute_etl_data()

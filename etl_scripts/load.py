import pandas as pd
from typing import Dict
from sqlalchemy import create_engine
from database.postgresql_db import PostgresqlDB
from logs.etl_log import ETLLogger

def load_data(dataset: pd.DataFrame, connection_params: Dict[str, any], table_name: str, schema: str, logger: ETLLogger):
    try:
        # make connection to postgresql
        postgresql_instance = PostgresqlDB(**connection_params)
        postgresql_instance.connect()
        logger.info("[DATA][ETL] connect to postgresql: success")
        # create sqlalchemy engine
        engine = create_engine(f"postgresql://{connection_params['username']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
        # write data to table
        dataset.to_sql(
            table_name,
            engine,
            schema=schema,
            if_exists="append",
            index=False
        )
    except Exception as ex:
        raise ex
    finally:
        # close connection to postgresql
        postgresql_instance.close()
        logger.info("[DATA][ETL] close to postgresql: success")
    
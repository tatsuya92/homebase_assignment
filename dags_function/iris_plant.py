from datetime import datetime, timedelta
from database.postgresql_db import PostgresqlDB
from database.clickhouse_db import ClickHouseDB

def transfer_data(**context):
    # get time run
    execution_date: datetime = context['execution_date']
    # query start time
    end_time = execution_date.replace(minute=0, second=0, microsecond=0)
    start_time = end_time - timedelta(hours=1)
    # get start 
    # connect to postgresql
    postgresql = PostgresqlDB()
    # connect to clickhousr
    click_house = ClickHouseDB()
    try:
        # get data from postgresql in 1 hours
        query = (
            "Select "
                "id, sepal_length, sepal_width, petal_length, petal_width, class, "
                "cast(created_at AS timestamp) as created_at, "
                "cast(modified_at AS timestamp) as modified_at "
            "from iris_plant.iris_plant "
            "where created_at >= '%s' and created_at < '%s'" %(start_time, end_time)
        )
        results = postgresql.execute_select_query(query)
        if not results:
            return
        # insert data to clickhouse
        query = "INSERT INTO iris_plant(id, sepal_length, sepal_width, petal_length, petal_width, class, created_at, modified_at) VALUES"
        click_house.execute_data(query, results)
    except Exception as ex:
        raise ex
    finally:
        postgresql.close()
        click_house.close()

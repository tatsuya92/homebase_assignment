from decouple import config
from clickhouse_driver import Client
from clickhouse_driver.errors import NetworkError

class ClickHouseDB:

    def __init__(
        self,
        host: str = None,
        username: str = None,
        password: str = None,
        database: str = None,
        port: int = None
    ):
        self.host = host or config('DB_CLICKHOUSE_HOST')
        self.port = port or config('DB_CLICKHOUSE_PORT', cast=int)
        self.username = username or config('DB_CLICKHOUSE_USERNAME')
        self.password = password or config('DB_CLICKHOUSE_PASSWORD')
        self.database = database or config('DB_CLICKHOUSE_DATABASE')
        self.client = None
    
    def connect(self):
        try:
            self.client = Client(
                host = self.host,
                port=self.port,
                user=self.username,
                # password=self.password,
                database=self.database
            )
        except NetworkError as ex:
            raise ex
    
    def execute_data(self, query, values):
        try:
            if not self.client:
                self.connect()
            self.client.execute(query, values, types_check=True)
        except Exception as ex:
            raise ex
    
    def close(self):
        if self.client:
            self.client.disconnect()
            
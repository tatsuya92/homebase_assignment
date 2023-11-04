import psycopg2
from decouple import config

class PostgresqlDB:

    def __init__(
        self,
        host: str = None,
        database: str = None,
        username = None,
        password = None,
        port: int = None
    ):
        self.host = host or config('DB_POSTGRE_HOST')
        self.port = port or config('DB_POSTGRE_PORT', cast=int)
        self.username = username or config('DB_POSTGRE_USERNAME')
        self.password = password or config('DB_POSTGRE_PASSWORD')
        self.database = database or config('DB_POSTGRE_DATABASE')
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host = self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                database=self.database
            )
            self.connection.autocommit = True
        except (Exception, psycopg2.Error) as error:
            raise error
    
    def create_cursor(self):
        if self.connection:
            self.cursor = self.connection.cursor()
    
    def execute_select_query(self, query):
        if not self.connection:
            self.connect()
        if not self.cursor:
            self.create_cursor()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as ex:
            raise ex
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

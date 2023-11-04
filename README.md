# homebase_assignment

PRE-REQUIREMENT:
 - install: python3.11
 - run: sql script in postgresql "Assigment/sql/postgre.sql" for creating database, schema and table
 - run: sql script in clickhouse "Assigment/sql/clickhouse.sql" for creating database and table

STEP:
 - cd: to project
 - create venv : python3.11 -m venv {venv_path}
 - correct: PYTHONPATH link to project
 - activate venv: source {venv_path}/bin/activate
 - install libs: pip install -r requirements.txt"
 - correct: database configuration params in "Assigment/.env"
 - change: "dags_folder" value in "airflow.cfg" file to "../Assigment/dags"

Task 1 and 2 :
  - Run: python Assigment/etl_scripts/main.py
Task 3:
  - SQL script: Assigment/sql/postgre.sql, Assigment/sql/clickhouse.sql
Task 4:
  - Dags folder: Assigment/dags
Task 5:
  - SQL script: Assigment/sql/clickhouse_queries.sql

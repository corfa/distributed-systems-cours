import psycopg2
from psycopg2 import sql
from fastapi import FastAPI
from urllib.parse import urlparse

url = urlparse("postgresql://postgres:mysecretpassword@postgres:5432/links")
db_params = {
    "dbname": url.path[1:],
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port,
}

def init_table():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS links (
        id SERIAL PRIMARY KEY,
        url TEXT NOT NULL,
        status INT
    );
    """
    cursor.execute(create_table_query)

    cursor.close()
    connection.commit()
    connection.close()


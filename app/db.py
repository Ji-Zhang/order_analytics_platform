import psycopg2
from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def connect_to_db():
    """Connect to the database."""
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    return connection

def run_query(query):
    """Run a SQL query and return the results."""
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
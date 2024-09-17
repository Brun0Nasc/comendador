import psycopg
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv("creds.env")  # Load environment variables from .env file

    dbName = os.getenv("DB_NAME")
    dbUser = os.getenv("DB_USER")
    dbPass = os.getenv("DB_PASSWORD")
    dbHost = os.getenv("DB_HOST")
    dbPort = os.getenv("DB_PORT")

    return f"dbname={dbName} user={dbUser} host={dbHost} password={dbPass} port={dbPort}"

def connect_database():
    conn = psycopg.connect(load_config())
    return conn
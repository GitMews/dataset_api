import configparser
import pymysql
from pathlib import Path

# Get conf file
CONFIG_FILE = Path("database.conf")

def load_database_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    return{"host": config["database"]["host"],
        "port": int(config["database"]["port"]),
        "user": config["database"]["user"],
        "password": config["database"]["password"],
        "name": config["database"]["name"],}

def get_connection():
    config = load_database_config()

    return pymysql.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["name"],
        cursorclass=pymysql.cursors.DictCursor)

def get_all():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM film")
            return cursor.fetchall()
    finally:
        conn.close()

def get_films():
    films = get_all()

    return [
        {
            "id": film["film_id"],
            "name": film["film_name"]
        }
        for film in films
    ]

def get_film_data(film_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM film WHERE film_id = %s",(film_id,))
            return cursor.fetchone()
    finally:
        conn.close()
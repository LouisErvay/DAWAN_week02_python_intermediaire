import sqlite3
from contextlib import contextmanager


# Context manager permet l'utilisation du mot clé yield, qui permet à son tour l'utilisation du with as autre part dans le code
@contextmanager
def database_connection(db_path):

    conn = sqlite3.connect(db_path)

    try:
        cursor = conn.cursor()

        yield cursor

    finally:
        conn.close()


with database_connection('database.db') as cursor:
    print("j'ai récupéré mon cursor")
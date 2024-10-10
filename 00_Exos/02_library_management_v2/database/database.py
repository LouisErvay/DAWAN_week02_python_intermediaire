import sqlite3
import logging
from contextlib import contextmanager

DATABASE_PATH = 'database.db'


class Database():
    def __init__(self):
        self.path = DATABASE_PATH

    @contextmanager
    def get_cursor(self):
        conn = sqlite3.connect(self.path)

        try:
            cursor = conn.cursor()

            yield cursor

        finally:
            conn.commit()
            conn.close()

    def create_tables(self):
        with self.get_cursor() as cursor:
            try:
                cursor.execute("""
                                CREATE TABLE IF NOT EXISTS user(
                                id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                name varchar(30) NOT NULL
                                )
                                """)

                cursor.execute("""
                                CREATE TABLE IF NOT EXISTS book(
                                id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                name varchar(30) NOT NULL,
                                author varchar(30) NOT NULL,
                                status BOOLEAN NOT NULL DEFAULT 0
                                )   
                                """)

                cursor.execute("""
                                CREATE TABLE IF NOT EXISTS loan (
                                id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                                user_id integer NOT NULL,
                                book_id integer NOT NULL
                                )
                                """)
            except Exception as e:
                print(f"Erreur lors de la création des tables: {e}")

    def auto_increment(self):
        users = [
            {'name': 'Didier'},
            {'name': 'Jeanne'},
            {'name': 'Eric'},
            {'name': 'Bouc'}
        ]

        books = [
            {'name': 'livre1', 'author': 'author1', 'status': 1},
            {'name': 'livre2', 'author': 'author2', 'status': 1},
            {'name': 'livre3', 'author': 'author3', 'status': 1},
            {'name': 'livre4', 'author': 'author4', 'status': 1}
        ]

        try:

            with self.get_cursor() as cursor:
                req = "INSERT INTO user VALUES (NULL, :name)"

                for u in users:
                    cursor.execute(req, u)
                    logging.info(f"Un utilisateur à été ajouté en db: {u['name']}")

                req = "INSERT INTO book VALUES (NULL, :name, :author, :status)"

                for b in books:
                    cursor.execute(req, b)
                    logging.info(f"Un livre à été ajouté en db: {b['name']}")
        except Exception as e:
            print(f"Erreur lors de l'incrémentation automatique des données: {e}")


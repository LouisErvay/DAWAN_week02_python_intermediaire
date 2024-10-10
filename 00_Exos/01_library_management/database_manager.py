import sqlite3
import logging
from contextlib import contextmanager

DATABASE_PATH = 'database.db'

@contextmanager
def database_connection(db_path):

    conn = sqlite3.connect(db_path)

    try:
        cursor = conn.cursor()

        yield cursor

    finally:
        conn.commit()
        conn.close()

def database_init():
    with database_connection(DATABASE_PATH) as cursor:

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
            logging.error(f"Erreur lors de la création des tables: {e}")

def increment_database():
    with database_connection(DATABASE_PATH) as cursor:

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

            with database_connection(DATABASE_PATH) as cursor:
                req = "INSERT INTO user VALUES (NULL, :name)"

                for u in users:
                    cursor.execute(req, u)
                    logging.info(f"Un utilisateur à été ajouté en db: {u['name']}")

                req = "INSERT INTO book VALUES (NULL, :name, :author, :status)"

                for b in books:
                    cursor.execute(req, b)
                    logging.info(f"Un livre à été ajouté en db: {b['name']}")

        except Exception as e:
            logging.error(f"Erreur lors de l'incrémentation auto de la db: {e}")

def add_user(user):

    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = "INSERT INTO user VALUES (NULL, :name)"
            cursor.execute(req, user)
            logging.info(f"Un utilisateur à été ajouté en db: {user['name']}")
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout d'un user: {e}")

def add_book(book):

    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = "INSERT INTO book VALUES (NULL, :name, :author, :status)"
            cursor.execute(req, book)
            logging.info(f"Un livre à été ajouté en db: {book['name']}")
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout d'un user: {e}")

def loan_book(loan):
    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = "INSERT INTO loan VALUES (NULL, :user_id, :book_id)"
            cursor.execute(req,loan)
            req = "UPDATE book SET status = 0 WHERE id = :book_id"
            cursor.execute(req, loan)
            logging.info(f"Ajout d'un loan entre le user id: {loan['user_id']} et le livre id: {loan['book_id']}")
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout un loan: {e}")

def return_book(book):
    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = "DELETE FROM loan WHERE book_id = :book_id"
            cursor.execute(req, book)
            req = "UPDATE book SET status = 1 WHERE id = :book_id"
            cursor.execute(req, book)
            logging.info(f"le livre id: {book['book_id']} a été rendu")
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout un loan: {e}")

def get_all_available_book():
    with database_connection(DATABASE_PATH) as cursor:

        try:
            req = "SELECT * FROM book WHERE status = 1"
            cursor.execute(req)
            return cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur lors de la récup des livres louées: {e}")

def get_all_non_available_book():
    with database_connection(DATABASE_PATH) as cursor:

        try:
            req = "SELECT * FROM book WHERE status = 0"
            cursor.execute(req)
            return cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur lors de la récup des livres non louées: {e}")

def get_all_user():
    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = "SELECT * FROM user"
            cursor.execute(req)
            return cursor.fetchall()
        except Exception as e:
            logging.error(f"Erreur lors de la récupérartion de tous les utilisateurs: {e}")

def get_all_loaned_book_from_user(user_id):
    with database_connection(DATABASE_PATH) as cursor:
        try:
            req = """SELECT book.* FROM book
                JOIN loan ON book.id = loan.book_id
                WHERE loan.user_id = :user_id
                """
            cursor.execute(req,user_id)
            return cursor.fetchall()
        except Exception as e:
            logging.error(f"Erreur lors de la récupérartion de l'utilisateur: {user_id} - erreur: {e}")
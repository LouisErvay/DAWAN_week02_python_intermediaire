from medias.i_media_manager import IMediaManager
from medias.i_media import IMedia
from medias.book import Book

from database.database import Database

from users.user import User

class BookManager(IMediaManager):
    def __init__(self):
        self.database = Database()

    def add_media(self, media: Book):
        book = media.__dict__
        book['status'] = 1 if book['status'] else 0
        with self.database.get_cursor() as cursor:
            try:
                req = "INSERT INTO book VALUES (NULL, :name, :author, :status)"
                cursor.execute(req, book)
                print(f"Un livre à été ajouté en db: {book['name']}")
            except Exception as e:
                print(f"Erreur lors de l'ajout d'un user: {e}")

    def loan_media(self, media: Book, user: User):
        loan = {'book_id': media.id, 'user_id': user.id}
        with self.database.get_cursor() as cursor:
            try:
                req = "INSERT INTO loan VALUES (NULL, :user_id, :book_id)"
                cursor.execute(req, loan)
                req = "UPDATE book SET status = 0 WHERE id = :book_id"
                cursor.execute(req, loan)
                print(f"Ajout d'un loan entre le user id: {loan['user_id']} et le livre id: {loan['book_id']}")
            except Exception as e:
                print(f"Erreur lors de l'ajout un loan: {e}")

    def return_media(self, media: Book):
        book = {'book_id': media.id}
        with self.database.get_cursor() as cursor:
            try:
                req = "DELETE FROM loan WHERE book_id = :book_id"
                cursor.execute(req, book)
                req = "UPDATE book SET status = 1 WHERE id = :book_id"
                cursor.execute(req, book)
                print(f"le livre id: {book['book_id']} a été rendu")
            except Exception as e:
                print(f"Erreur lors de l'ajout un loan: {e}")

    def get_books_from_db(self, req: str):
        with self.database.get_cursor() as cursor:
            try:
                cursor.execute(req)
                return [Book(id=row[0], name=row[1], author=row[2], status=bool(row[3])) for row in cursor.fetchall()]

            except Exception as e:
                print(f"Erreur lors de la récup de tous les livres: {e}")

    def get_all(self) -> [IMedia]:
        return self.get_books_from_db(req="SELECT * FROM book")

    def get_all_available(self) -> [IMedia]:
        return self.get_books_from_db(req="SELECT * FROM book WHERE status = 1")

    def get_all_non_available(self) -> [IMedia]:
        return self.get_books_from_db(req="SELECT * FROM book WHERE status = 0")

    def get_all_loaned_from_user(self, user: User) -> [IMedia]:
        user_id = {'user_id': user.id}
        with self.database.get_cursor() as cursor:
            try:
                req = """SELECT book.* FROM book
                                JOIN loan ON book.id = loan.book_id
                                WHERE loan.user_id = :user_id
                                """
                cursor.execute(req, user_id)
                data = cursor.fetchall()

                return [Book(id=row[0], name=row[1], author=row[2], status=bool(row[3])) for row in data]

            except Exception as e:
                print(f"Erreur lors de la récup de tous les livres: {e}")

    def ask_for_a_book(self, books: [Book]):
        print("Voici la liste des livres :")
        for book in books:
            print(book.__dict__)

        while True:
            id_selected = int(input(f"Sélectionnez l'ID du livre:"))
            for book in books:
                if id_selected == book.id:
                    return book
            else:
                print("un id qui est dans la liste on a dit !")
from users.user_manager import UserManager
from users.user import User

from database.database import Database

from medias.book_manager import BookManager
from medias.book import Book

def main():
    database = Database()
    # database.create_tables()
    # database.auto_increment()

    user_manager = UserManager()
    book_manager = BookManager()

    while True:
        choix = input("""--- menu ---
    1. ajouter un livre
    2. ajouter un utilisateur
    3. emprunter un livre
    4. rendre un livre
    5. lister les livres empruntés
    6. Lister les livres disponibles
    7. lister les emprunts d'un utilisateur
    8. quitter""")

        if choix == "8":
            break

        match choix:
            case "1":
                book_manager.add_media(media=Book(id=0, name=input("Nom: "), author=input("Auteur:"), status=True))

            case "2":
                user_manager.add_user(user=User(id=0, name=input("Nom: ")))

            case "3":
                book = book_manager.ask_for_a_book(books=book_manager.get_all_available())
                user = user_manager.ask_for_a_user(users=user_manager.get_all_user())

                book_manager.loan_media(media=book, user=user)

            case "4":
                book = book_manager.ask_for_a_book(books=book_manager.get_all_non_available())

                book_manager.return_media(media=book)

            case "5":
                for book in book_manager.get_all_non_available():
                    print(book.__dict__)

            case "6":
                for book in book_manager.get_all_available():
                    print(book.__dict__)

            case "7":
                book_manager.get_all_loaned_from_user(user=user_manager.ask_for_a_user(users=user_manager.get_all_user()))

if __name__ == '__main__':
    main()

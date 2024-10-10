import logging_config
import logging
from database import database_manager
import my_func

def add_book():
    name = input("le nom de l'utilisateur ?")
    user = {"name": name}
    database_manager.add_user(user)

def add_user():
    name = input("le nom du livre ?")
    author = input("Le nom de l'autheur ?")
    status = 0
    while True:
        status = int(input("""Le livre est actuellement disponible à l'emprunt ?
                            0. Non
                            1. Oui"""))
        if status == 0 or 1:
            break
    book = {"name": name, "author": author, "status": status}
    database_manager.add_book(book)

def loan_a_book(user_list, book_list):
    user_id_selected = my_func.select_user(user_list)

    book_id_selected = my_func.select_book(book_list)

    loan = {"user_id": user_id_selected, "book_id": book_id_selected}
    database_manager.loan_book(loan)

def return_a_book(book_list):

    book_id_selected = my_func.select_book(book_list)

    book_id = {"book_id": book_id_selected}
    database_manager.return_book(book_id)


def list_non_available_book():
    data = database_manager.get_all_non_available_book()
    if data == []:
        print("Aucun livre n'est loué !")
    else:
        for book in data:
            print(book)

def list_available_book():
    data = database_manager.get_all_available_book()
    if data == []:
        print("Tous les livres sont loués !")
    else:
        for book in data:
            print(book)


if __name__ == "__main__":

    database_manager.database_init()

    while True:
        choix = input("""--- menu ---
1. ajouter un livre
2. ajouter un utilisateur
3. emprunter un livre
4. rendre un livre
5. lister les livres empruntés
6. Lister les livres disponibles
7. lister les emprunts d'un utilisateur
8. Remplir la database
9. quitter""")

        if choix == "9":
            break

        match choix:
            case "1":
                add_book()

            case "2":
                add_user()

            case "3":
                user_list = database_manager.get_all_user()
                book_list = database_manager.get_all_available_book()

                if user_list == [] or book_list == []:
                    print("Manque de data pour faire cette opération")
                    break

                loan_a_book(user_list, book_list)

            case "4":
                book_list = database_manager.get_all_non_available_book()

                if book_list == []:
                    print("aucun book n'est loué, rien a rendre")
                    break

                return_a_book(book_list)

            case "5":
                list_non_available_book()

            case "6":
                list_available_book()

            case "7":
                user_list = database_manager.get_all_user()
                if user_list == []:
                    print("aucun utilisateur dans la db, action impossible")
                    break

                user_id_selected = my_func.select_user(user_list)

                data = database_manager.get_all_loaned_book_from_user({"user_id":user_id_selected})
                print(data)
            case "8":
                database_manager.increment_database()
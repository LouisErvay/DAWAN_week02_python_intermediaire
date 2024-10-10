def select_user(users):
    user_ids = [user[0] for user in users]
    print("Voici la liste des utilisateurs :")
    for user in users:
        print(user)
    while True:
        id_selected = int(input(f"Sélectionnez l'ID de l'utilisateur:"))
        if id_selected in user_ids:
            return id_selected
        else:
            print("un id qui est dans la liste on a dit !")

def select_book(books):
    book_ids = [user[0] for user in books]
    print("Voici la liste des livres :")
    for user in books:
        print(user)
    while True:
        id_selected = int(input(f"Sélectionnez l'ID du livre:"))
        if id_selected in book_ids:
            return id_selected
        else:
            print("un id qui est dans la liste on a dit !")
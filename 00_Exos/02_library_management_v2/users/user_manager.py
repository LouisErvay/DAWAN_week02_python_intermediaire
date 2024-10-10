from users.user import User
from database.database import Database

class UserManager():
    def __init__(self):
        self.database = Database()

    def add_user(self, user: User):
        with self.database.get_cursor() as cursor:
            user = user.__dict__
            try:
                req = "INSERT INTO user VALUES (NULL, :name)"
                cursor.execute(req, user)
                print(f"Un utilisateur à été ajouté en db: {user['name']}")
            except Exception as e:
                print(f"Erreur lors de l'ajout d'un user: {e}")

    def get_all_user(self) -> [User]:
        with self.database.get_cursor() as cursor:
            try:
                req = "SELECT * FROM user"
                cursor.execute(req)
                return [User(id, name) for id, name in cursor.fetchall()]
            except Exception as e:
                print(f"Erreur lors de la récupérartion de tous les utilisateurs: {e}")

    def ask_for_a_user(self, users: [User]) -> User:
        print("Voici la liste des utilisateurs :")
        for user in users:
            print(user.__dict__)

        while True:
            id_selected = int(input(f"Sélectionnez l'ID de l'utilisateur: "))
            # Recherche de l'utilisateur par ID
            for user in users:
                if user.id == id_selected:
                    return user  # Retourne l'instance de User
            else:
                print("Un ID qui est dans la liste on a dit !")
from user.user_factory import UserFactory


def main():
    
    choice = input("Choisir un type de nouvel utilisateur")
    name = input("Donner son nom")
    address = print("Donner son address")
    
    
    new_admin = UserFactory.createUser("Bob", "48 rue blabla", "Admin")
    
    new_customer = UserFactory.createUser("Thérése", "55 bd ...", "Customer")
    
    return [new_admin, new_customer]


if __name__ == "__main__":
    main()
from users.UserFactory import UserFactory

def main():

    name = input('Name: ')
    address = input('Address: ')
    type = input('Choisir un type de nouvel utilisateur: ')

    new_admin = UserFactory.create_user(name, address, type)
    new_customer = UserFactory.create_user("Dylan", "48 avenue des champs", "Customer")

    return [new_admin, new_customer]

if __name__ == '__main__':
    print(main())
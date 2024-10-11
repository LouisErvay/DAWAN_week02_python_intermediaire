from admin import Admin
from customer import Customer


class UserFactory:
    
    @staticmethod
    def createUser(name, address, user_type):
        if user_type.lower() == "admin":
            return Admin(name, address)
        elif user_type.lower() == "customer":
            return Customer(name, address)
        else:
            raise ValueError(f"Type d'utilisateur inconnu")
from users.Admin import Admin
from users.Customer import Customer

class UserFactory:

    def __init__(self, url_db) -> None:
        self.url_db = url_db

    @staticmethod
    def create_user(name, address, user_type):
        if user_type.lower() == "admin":
            return Admin(name, address)
        elif user_type.lower() == "customer":
            return Customer(name, address)
        else:
            raise ValueError("Invalid user_type")
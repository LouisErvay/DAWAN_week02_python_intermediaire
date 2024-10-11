from users.IUser import IUser

class Admin(IUser):

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def __str__(self) -> str:
        return f"{self.name} - {self.address}"
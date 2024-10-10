from users.i_user import IUser

class User(IUser):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name: str = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.nam = name


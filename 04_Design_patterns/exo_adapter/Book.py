class Book:

    def __init__(self, title, author, description) -> None:
        self.title = title
        self.author = author
        self.description = description

    def __str__(self) -> str:
        return f"""
{self.title} est un livre de {self.author}
Description:
    {self.description}
"""
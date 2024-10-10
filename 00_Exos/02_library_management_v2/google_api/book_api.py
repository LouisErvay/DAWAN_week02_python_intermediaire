import requests

# https://www.googleapis.com/books/v1/volumes?q=

class BookApi():
    def __init__(self):
        pass

    def get_book(self, livre: str):
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={livre}")
        data = response.json() if response.ok else None

from GoogleBooksApi import GoogleBooksAPI
from GoogleBooksAdapter import GoogleBooksAdapter

def main():
    google_books_api = GoogleBooksAPI()
    google_books_data = google_books_api.search_by_title(input("Quel livre voulez-vous récupérer? "))
    google_book_adapter = GoogleBooksAdapter(google_books_data)
    book = google_book_adapter.adapt_to_book()

    print(book)

if __name__ == '__main__':
    main()
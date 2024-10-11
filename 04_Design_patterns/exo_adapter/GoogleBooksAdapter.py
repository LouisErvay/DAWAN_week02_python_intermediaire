from Book import Book

class GoogleBooksAdapter:
    def __init__(self, google_books_data) -> None:
        self.google_books_data = google_books_data
    
    def adapt_to_book(self) -> Book:
        # Extraction des données pertinentes
        title = self.google_books_data.get('title', 'Titre non disponible')
        authors = self.google_books_data.get('authors', ['Auteur inconnu'])
        description = self.google_books_data.get('description', 'Pas de description')

        # Création d'un objet book avec les données adaptées
        return Book(title, ', '.join(authors), description)
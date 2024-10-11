import requests

class GoogleBooksAPI:
    
    BASE_URL = "https://www.googleapis.com/books/v1/volumes?q="

    def search_by_title(self, title):
        url = f"{self.BASE_URL}{title}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                return data['items'][0]['volumeInfo']  # Prend le premier résultat
            else:
                print(f"Aucun livre trouvé pour '{title}' sur Google Books.")
                return None
        else:
            print("Erreur lors de l'appel à l'API Google Books.")
            return None
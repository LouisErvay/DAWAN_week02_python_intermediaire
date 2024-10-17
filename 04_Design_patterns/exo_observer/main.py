from users.User import User
from medias.Book import Book
from medias.Magazine import Magazine

def main():

    book = Book("Les misérables", "Victor Hugo")
    magazine = Magazine("Tête-à-tête avec Noémie Merlant, grande promesse du cinéma français", "Manon Garrigues (VOGUE)")
    mael = User("Mael", "BELLIARD")
    jean = User("Jean", "DUPONT")
    
    book.attach(mael)
    magazine.attach(mael)
    magazine.attach(jean)
    
    print(">>>>>>> Suivi des disponibilités:")

    book.set_available(True)
    magazine.set_available(True)

if __name__ == '__main__':
    main()
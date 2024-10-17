from medias.MediaFactory import MediaFactory

def main():

    title = input('Title: ')
    author = input('Author: ')
    type = input('Choisir un type de media: ')

    new_media = MediaFactory.create_media(title, author, type)
    new_book = MediaFactory.create_media("Les misérables", "Victor Hugo", "Book")

    print(new_media)
    print(new_book)

if __name__ == '__main__':
    main()
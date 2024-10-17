from media_factory.book_factory import BookFactory

from user.user import User
def main():

    book_factory = BookFactory()


    book1 = book_factory.create_media(name="livre1", author="auth1", available=True)

    book2 = book_factory.create_media(name="livre2", author="auth2", available=False)

    user = User(name="user1")

    book2.attach(observer=user)

    book2.set_available(available=True)

    print(book1.get_name())


if __name__ == "__main__":
    main()
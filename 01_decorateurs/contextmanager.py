from contextlib import contextmanager

# Context manager avec une class
# Nécéssite l'implémentation des methodes __enter__ et __exit__

class AutoFileManager:
    file = None
    def __enter__(self):
        self.file = open("test.txt", "r", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.file.closed:
            self.file.close()

with AutoFileManager() as file:
    x = file.read()
    print(x)


# Avec une Fonction
# Context manager permet l'utilisation du mot clé yield, qui permet à son tour l'utilisation du with as autre part dans le code
@contextmanager
def database_connection():
    file = None
    try:
        file = open("test.txt", "r", encoding="utf-8")
        yield file
    finally:
        if not file.closed:
            file.close()

with database_connection() as file:
    x = file.read()
    print(x)



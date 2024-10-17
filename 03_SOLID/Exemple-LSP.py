"""
    L : Liskov Substitution principle (LSP) : Les objets d’une sous classe doivent pouvoir remplacer les objets de la classe de base sans modifier le comportement attendu 
"""

class Vehicle:
    def start_engine(self):
        print("Moteur démarré.")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Moteur électrique démarré.")

class PetrolCar(Vehicle):
    def start_engine(self):
        print("Moteur à essence démarré.")


def start(vehicle):
    vehicle.start_engine()
    

voiture = Vehicle()
nissan = PetrolCar()
renault = ElectricCar()


start(renault)

"""Contre exemple, ne respectant pas le LSP :
    Supposons que nous ayons une classe Rectangle avec deux attributs, la largeur et la hauteur. Puis, nous créons une sous-classe Square (carré) qui hérite de Rectangle. 
    Cependant, un carré doit avoir ses deux côtés égaux, donc cela modifie le comportement attendu d'un rectangle.

"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height



def resize_rectangle(rect: Rectangle):
    rect.set_width(10)
    rect.set_height(5)
    print(f"Nouvelle surface: {rect.get_area()}")

# Utilisation avec un Rectangle (comportement attendu)
rectangle = Rectangle(2, 3)
resize_rectangle(rectangle)  # Affiche: Nouvelle surface: 50

# Utilisation avec un Square (comportement inattendu)
square = Square(5)
resize_rectangle(square)  # Comportement incorrect : la largeur et la hauteur sont modifiées simultanément

"""Dans l'exemple ci-dessus, l'appel à resize_rectangle(square) ne produit pas le comportement attendu pour un rectangle, car les deux côtés du carré sont modifiés simultanément. 
    Cela ne respecte pas le principe LSP, car la sous-classe Square ne peut pas remplacer la classe de base Rectangle sans changer le comportement.
"""

"""
Encapsulation : C'est le fait de regrouper les données (attributs) et les méthodes (fonctions) qui les utilisent au sein d'un même objet. 
Cela protège les données et contrôle comment elles sont accédées ou modifiées.
"""

class Person:
    def __init__(self, name, age):
        self.__name = name  # Attribut privé
        self.__age = age    # Attribut privé

    # Getter pour accéder à l'attribut name
    def get_name(self):
        return self.__name

    # Setter pour modifier l'attribut name
    def set_name(self, name):
        self.__name = name

    # Getter pour accéder à l'attribut age
    def get_age(self):
        return self.__age

    # Setter pour modifier l'attribut age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("L'âge ne peut pas être négatif")

# Exemple d'utilisation
person = Person("Alice", 30)
print(person.get_name())  # Affiche: Alice

person.set_age(35)        # Modifie l'âge
print(person.get_age())   # Affiche: 35
 
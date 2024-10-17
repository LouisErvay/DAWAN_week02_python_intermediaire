"""
Héritage : Cela permet de créer de nouvelles classes basées sur des classes existantes. 
La nouvelle classe hérite des attributs et des méthodes de la classe parente, ce qui évite de réécrire du code déjà existant."""

class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Nom : {self.name}"

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)  # Appel du constructeur de la super-classe
        self.salary = salary

    # Surcharge de la méthode get_info
    def get_info(self):
        return f"Nom : {self.name}, Salaire : {self.salary}"

# Exemple d'utilisation
employee = Employee("Charlie", 6000)
print(employee.get_info())  # Affiche: Nom : Charlie, Salaire : 6000
  
  
class User(Person):
    def __init__(self, name, achats):
        super().__init__(name)
        self.achats = achats
        
    def get_info(self):
        return f"Nom : {self.name}, {self.achats}"

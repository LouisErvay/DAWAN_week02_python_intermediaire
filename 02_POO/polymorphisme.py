"""Polymorphisme : C'est la capacité d'utiliser une même interface ou méthode pour des objets de classes différentes. 
En d'autres termes, une même action peut se comporter différemment selon l'objet qui l'exécute."""



from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_info(self):
        pass


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_info(self):
        return f"Nom : {self.name}, Salaire : {self.salary}"

class Manager(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    # def get_info(self): Si cette méthode n'est pas accessible c'est celle de la classe parente qui sera utilisée.
    #     return f"Nom : {self.name}, Salaire : {self.salary}"

    

# Fonction polymorphique
def display_info(person):
    print(person.get_info())

# Exemple d'utilisation
person = Person("Alice")
employee = Employee("Bob", 5000)
manager = Manager("Carol", "IT")

display_info(person)   # Affiche: Nom : Alice
display_info(employee) # Affiche: Nom : Bob, Salaire : 5000
display_info(manager)  # Affiche: Nom : Carol, Département : IT

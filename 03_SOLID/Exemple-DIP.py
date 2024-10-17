"""D : Dependency inversion principle : les modules de haut niveau ne doivent pas dépendre de module de bas niveau, le deux doivent dépendre d’abstraction. Les détails d'implémentation doivent dépendre des notions de haut niveau.
"""
from abc import ABC, abstractmethod

# Interface pour interagir avec la base de données
class DbService(ABC):
    @abstractmethod
    def save_employee(self, employee):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass

    @abstractmethod
    def find_employee(self, employee_id):
        pass


# Implémentation de DbService pour MySQL (dépend de DBService)
class MySqlService(DbService):
    def save_employee(self, employee):
        print(f"Enregistrement de l'employé {employee['name']} dans MySQL")

    def delete_employee(self, employee_id):
        print(f"Suppression de l'employé avec l'ID {employee_id} de MySQL")

    def find_employee(self, employee_id):
        print(f"Recherche de l'employé avec l'ID {employee_id} dans MySQL")
        # Simuler un employé trouvé
        return {"id": employee_id, "name": "John Doe", "position": "Developer"}


# Implémentation de DbService pour PostgreSQL (dépend de DBService)
class PostgresService(DbService):
    def save_employee(self, employee):
        print(f"Enregistrement de l'employé {employee['name']} dans PostgreSQL")

    def delete_employee(self, employee_id):
        print(f"Suppression de l'employé avec l'ID {employee_id} de PostgreSQL")

    def find_employee(self, employee_id):
        print(f"Recherche de l'employé avec l'ID {employee_id} dans PostgreSQL")
        # Simuler un employé trouvé
        return {"id": employee_id, "name": "Jane Doe", "position": "Manager"}


class Employee:
    def __init__(self, db_service: DbService): #Employee depend de l'interface DBService mais pas de ses implémentations
        self.db_service = db_service

    def add_employee(self, employee_data):
        self.db_service.save_employee(employee_data)

    def remove_employee(self, employee_id):
        self.db_service.delete_employee(employee_id)

    def get_employee(self, employee_id):
        employee = self.db_service.find_employee(employee_id)
        print(f"Employé trouvé : {employee['name']}, Poste : {employee['position']}")


        """
        Employee -> DBService<Interface> <- MySqlService 
        """
#Dans main

# Utilisation de MySqlService
mysql_service = MySqlService()
employee_manager = Employee(mysql_service)

employee_manager.add_employee({"id": 1, "name": "Alice", "position": "Engineer"})
employee_manager.get_employee(1)
employee_manager.remove_employee(1)

# Utilisation de PostgresService
postgres_service = PostgresService()
employee_manager = Employee(postgres_service)

employee_manager.add_employee({"id": 2, "name": "Bob", "position": "Designer"})
employee_manager.get_employee(2)
employee_manager.remove_employee(2)

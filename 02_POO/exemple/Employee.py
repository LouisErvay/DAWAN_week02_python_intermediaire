
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def save_to_db(self):
        """Simule l'enregistrement de l'employé dans une base de données."""
        print(f"Saving {self.name} with salary {self.salary} to the database.")
        # Logique d'enregistrement dans la base de données ici

    def save_to_xml(self):
        """Simule l'enregistrement de l'employé au format XML."""
        print(f"Saving {self.name} with salary {self.salary} to an XML file.")
        # Logique pour enregistrer en XML ici

    def process_payment(self):
        """Simule le paiement de l'employé."""
        print(f"Processing payment for {self.name}. Salary: {self.salary}.")
        # Logique de gestion du paiement ici

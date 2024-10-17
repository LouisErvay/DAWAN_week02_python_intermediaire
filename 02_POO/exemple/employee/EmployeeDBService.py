from Employee import Employee

class EmployeeDBService:
    """Service dédié à la gestion des employés dans la base de données."""
    
    def save_to_db(self, employee: Employee):
        print(f"Saving {employee.name} with salary {employee.salary} to the database.")
        # Logique d'enregistrement dans la base de données
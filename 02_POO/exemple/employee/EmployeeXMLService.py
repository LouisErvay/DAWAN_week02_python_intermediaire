from Employee import Employee

class EmployeeXMLService:
    """Service dédié à l'enregistrement des employés en XML."""
    
    def save_to_xml(self, employee: Employee):
        print(f"Saving {employee.name} with salary {employee.salary} to an XML file.")
        # Logique pour enregistrer en XML
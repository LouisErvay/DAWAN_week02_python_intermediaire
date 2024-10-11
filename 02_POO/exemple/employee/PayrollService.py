from Employee import Employee

class PayrollService:
    """Service dédié à la gestion de la paie des employés."""
    
    def process_payment(self, employee: Employee):
        print(f"Processing payment for {employee.name}. Salary: {employee.salary}.")
        # Logique de gestion du paiement

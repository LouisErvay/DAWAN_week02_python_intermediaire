from employee import Employee, EmployeeDBService, EmployeeXMLService, PayrollService



# Création d'un employé
employee = Employee("John Doe", 5000.0)

# Utilisation des services pour les actions spécifiques
db_service = EmployeeDBService()
xml_service = EmployeeXMLService()
payroll_service = PayrollService()

# Enregistrer l'employé dans la base de données
db_service.save_to_db(employee)

# Enregistrer l'employé au format XML
xml_service.save_to_xml(employee)

# Traiter le paiement de l'employé
payroll_service.process_payment(employee)

"""I : Interface Segregation Principle : les interfaces doivent être spécifique au client, une classe ne doit pas être forcée d’implémenter des méthodes dont elle n’a pas besoin.
"""

# Interface de base pour les véhicules
class IVehicle:
    def start(self):
        pass


# Interface spécifique pour les véhicules volants
class IFlyable:
    def fly(self):
        pass

# Voiture implémente seulement IVehicle
class Car(IVehicle):
    def start(self):
        print("La voiture démarre.")
    

# Avion implémente IVehicle et IFlyable
class Airplane(IVehicle, IFlyable):
    def start(self):
        print("L'avion démarre.")
    
    def fly(self):
        print("L'avion vole.")

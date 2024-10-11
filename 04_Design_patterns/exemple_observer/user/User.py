from observer.IObserver import IObserver

class User(IObserver):
    def __init__(self, name, email):
        self.name = name
        self.email = email
          
    def update(self, delivery_status):
        print(f"Notification pour {self.name} : la livraison est en status : {delivery_status}")
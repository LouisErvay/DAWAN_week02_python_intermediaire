from observer.ISubject import ISubject

class Delivery(ISubject):
    
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.status = "Commande reçue"
        self.observers = []
        
    
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        if observer not in self.observers:
            self.observers.remove(observer)
    
    
    def notify(self):
        for observer in self.observers:
            observer.update(self.status)
              
    def update_status(self, new_status):
        self.status = new_status
        self.notify()
        
    def get_status(self):
        return self.status
    
    def get_tracking_number(self):
        return self.tracking_number
from observer.i_subject import ISubject

from observer.i_observer import IObserver

class Delivery(ISubject):

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.status = "Commande en cours de livraison.."
        self.observers: [IObserver] = []

    def attach(self, observer: IObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.status)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        self.notify()

    def get_tracking_number(self):
        return self.tracking_number

    def set_tracking_number(self, tracking_number):
        self.tracking_number = tracking_number
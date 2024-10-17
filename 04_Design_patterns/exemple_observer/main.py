from delivery.Delivery import Delivery
from user.User import User

def main():
    
    delivery = Delivery("1234ABC")
    print(f"Suivi lde la livraison : {delivery.get_tracking_number}")
    
    
    user_alice = User("Alice", "alice@gmail.com")
    user_bob = User("Bob", "bob@exemple.com")
    
    delivery.attach(user_alice)
    delivery.attach(user_bob)
    
    
    print("Mise à jour du statut de livraison :")
    
    delivery.update_status("Colis expédié")
    delivery.update_status("En cours de livraison")
    delivery.update_status("Colis livré")
    
    
if __name__ == "__main__":
    
    main()
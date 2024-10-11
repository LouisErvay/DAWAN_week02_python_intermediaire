from delivery.delivery import Delivery
from user.user import User

def main():
    delivery = Delivery("123ABC")
    print(f"Suivi le la livraison numéro: {delivery.get_tracking_number()}")

    user1 = User(name="Jean", email="jean.gmoil.com")
    user2 = User(name="Alice", email="alice.gmoil.com")

    delivery.attach(user1)

    delivery.set_status(status="Commande arrivée !")

if __name__ == "__main__":
    main()
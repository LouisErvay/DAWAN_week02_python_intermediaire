class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        if prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self.prix = prix

    def get_prix(self):
        return self.prix

    def appliquer_remise(self, pourcentage):
        if pourcentage < 0 or pourcentage > 100:
            raise ValueError("Le pourcentage de remise doit être compris entre 0 et 100")
        self.prix = self.prix * (1 - pourcentage / 100)
 
 
        """
            Écrire un test unitaire pour la classe Produit qui vérifie que :

            La remise est correctement appliquée.
            Une exception est levée pour un prix ou un pourcentage négatif.
        """
        
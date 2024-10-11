class Inventaire:
    def __init__(self):
        self.produits = {}

    def ajouter_produit(self, nom, quantite):
        if nom in self.produits:
            self.produits[nom] += quantite
        else:
            self.produits[nom] = quantite

    def retirer_produit(self, nom, quantite):
        if nom not in self.produits or self.produits[nom] < quantite:
            raise ValueError("Quantité insuffisante ou produit non existant")
        self.produits[nom] -= quantite

    def obtenir_quantite(self, nom):
        return self.produits.get(nom, 0)


        """Écrire un test unitaire pour vérifier :

    L'ajout correct de produits dans l'inventaire.
    Le retrait de quantités.
    La gestion des erreurs en cas de quantité insuffisante ou de produit inexistant.
        """
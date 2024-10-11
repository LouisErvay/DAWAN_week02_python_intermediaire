class Utilisateur:
    def __init__(self, nom, mot_de_passe):
        self.nom = nom
        self.mot_de_passe = mot_de_passe

    def changer_mot_de_passe(self, ancien_mdp, nouveau_mdp):
        if ancien_mdp != self.mot_de_passe:
            raise ValueError("Ancien mot de passe incorrect")
        if len(nouveau_mdp) < 6:
            raise ValueError("Le nouveau mot de passe doit comporter au moins 6 caractères")
        self.mot_de_passe = nouveau_mdp



        """Écrire un test unitaire pour :

    Vérifier que le changement de mot de passe fonctionne.
    Vérifier qu'une exception est levée pour un ancien mot de passe incorrect ou un nouveau mot de passe trop court.
        """
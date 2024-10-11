class CompteBancaire:

    def __init__(self, name, solde) -> None:
        self.name = name
        self.solde = solde

    def get_solde(self):
        return self.solde

    def depot(self, amount) -> None:
        if amount < 0:
            raise ValueError("The amount can't be inferior to 0")
        
        self.solde += amount


    def retrait(self, amount) -> None:
        if amount > self.solde:
            raise ValueError("The amount can't be superior of the solde")
        
        self.solde -= amount
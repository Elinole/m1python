class CompteBancaire:
    def __init__(self, name, solde):
        self.name = name
        self.solde = solde

    def depot(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        if (somme > self.solde):
            print("Vous ne pouvez pas retirer", somme, "car vous n'avez que", self.solde, "euros")
        else:
            self.solde = self.solde - somme

    def affiche(self):
        print("Le solde du compte bancaire de", self.name, "est de", self.solde, "euros")

c1 = CompteBancaire("Elias", 1000)

c1.retrait(1001)
c1.affiche()
class DateNaissance:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def ToString(self):
        self.jour = format(self.jour, '02')
        self.mois = format(self.mois, '02')
        return self.jour, "/", self.mois, "/", self.annee

# d1 = DateNaissance(2, 3, 1998)
# print(d1.ToString())

class Personne(DateNaissance):
    def __init__(self, nom, prenom, DateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.jour = DateNaissance.jour
        self.mois = DateNaissance.mois
        self.annee = DateNaissance.annee
    
    def Afficher(self):
        print(
            "Nom :", self.nom, "\n"
            "Prénom :", self.prenom, "\n"
            "Date de naissance :", self.ToString()
        )

class Employe(Personne):
    def __init__(self, nom, prenom, DateNaissance, salaire):
        self.nom = nom
        self.prenom = prenom
        self.jour = DateNaissance.jour
        self.mois = DateNaissance.mois
        self.annee = DateNaissance.annee
        self.salaire = salaire

    def Afficher(self):
        self.salaire = round(self.salaire, 2)
        print(
            "Nom :", self.nom, "\n"
            "Prénom :", self.prenom, "\n"
            "Date de naissance :", self.ToString(), "\n"
            "Salaire :", self.salaire
        )

class Chef(Employe):
    def __init__(self, nom, prenom, DateNaissance, salaire, service):
        self.nom = nom
        self.prenom = prenom
        self.jour = DateNaissance.jour
        self.mois = DateNaissance.mois
        self.annee = DateNaissance.annee
        self.salaire = salaire
        self.service = service

    def Afficher(self):
        self.salaire = round(self.salaire, 2)
        print(
            "Nom :", self.nom, "\n"
            "Prénom :", self.prenom, "\n"
            "Date de naissance :", self.ToString(), "\n"
            "Salaire :", self.salaire, "\n"
            "Service :", self.service
        )

# P = Personne("Ilyass", "MATH", DateNaissance(1,7,1982))
# P.Afficher()

# E=Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
# E.Afficher()

Ch=Chef("Ilyass","Math",DateNaissance(1,7,1988),7865.548,"Ressources humaines")
Ch.Afficher()
def salaire_mensuel(salaire_annuel):
    result = int(salaire_annuel)/12
    return result

def salaire_hebdomadaire(salaire_mensuel):
    return int(salaire_mensuel)/4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return int(salaire_hebdomadaire)/int(heures_travaillees)

salaire_an = input("Veuillez saisir votre salaire à l'année : ")
nb_heure = input("Veuillez saisir le nombre d'heures travaillées par semaine : ")

salaire_mois = salaire_mensuel(salaire_an)
salaire_hebdo = salaire_hebdomadaire(salaire_mois)
salaire_heure = salaire_horaire(salaire_hebdo, nb_heure)

print(f"Votre taux horaire est de {salaire_heure} €")
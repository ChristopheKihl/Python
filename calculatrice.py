nombre1 = int(input("Veuillez entrer un premier nombre : "))
nombre2 = int(input("Veuillez entrer un second nombre : "))

def calulator(nb1, nb2):
    result = nb1 + nb2
    return result

resultat = calulator(nombre1, nombre2)

print(f"Le resultat de l'addition de {nombre1} avec {nombre2} est égal à {resultat}") 
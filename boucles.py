liste = []
somme = 0

for i in range(4):
    nombre = input("Veuillez saisir un nombre : ")
    liste.append(nombre)

for nombres in liste:
    somme += int(nombres)

print(f"La somme des nombres dans la liste est de {somme}")

moyenne = somme / len(liste)

print(f"La moyenne des nombres dans la liste est de {moyenne}")

for nombres in liste:
    if(float(nombres) > moyenne):
        print(f"Le nombre {nombres} dans la iste est supérieur la moyenne")


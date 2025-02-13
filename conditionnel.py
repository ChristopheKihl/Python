nombre1 = input("Veuillez saisir un premier nombre : ")
nombre2 = input("Veuillez saisir un second nombre : ")

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    operation = input("Veuillez entrer l'opérateur : ")
else:
    raise SystemExit("Les nombres ne sont pas de type numérique")

if operation == "+" or operation == "-" or operation == "/" or operation == "*":
        match operation:
            case "+":
                result = nombre1 + nombre2
                print(f"{nombre1} + {nombre2} = {result}")
            case "-":
                result = nombre1 - nombre2
                print(f"{nombre1} - {nombre2} = {result}")
            case "*":
                result = nombre1 * nombre2
                print(f"{nombre1} * {nombre2} = {result}")
            case "/":
                if nombre2 > 0:
                    result = nombre1 / nombre2
                    result =round(result, 2)
                    print(f"{nombre1} / {nombre2} = {result}")
                else:
                    raise SystemExit("Division par 0 impossible")
else:
    raise SystemExit("L'opérateur n'est pas conforme")
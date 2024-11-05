def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))
    except Erreur:
        print("Entrée invalide. Veuillez entrer des nombres valides.")
        return
    
    operation = input("Entrez l'opération (+, -, *, /) : ")

    
    if operation == "+":
        resultat = nombre1 + nombre2
        print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
    elif operation == "-":
        resultat = nombre1 - nombre2
        print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
    elif operation == "*":
        resultat = nombre1 * nombre2
        print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
    elif operation == "/":
        if nombre2 == 0:
            print("Erreur : Division par zéro n'est pas permise.")
        else:
            resultat = nombre1 / nombre2
            print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
    else:
        print("Opération non reconnue. Veuillez entrer +, -, *, ou /.")


calculatrice()

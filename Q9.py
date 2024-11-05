def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
while True:
    nombre = int(input("Entrez un nombre entier positif pour calculer sa factorielle : "))
    if nombre >= 0:
        break
    else:
        print("Erreur : le nombre doit être positif. Veuillez essayer à nouveau.")

resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est :", resultat)

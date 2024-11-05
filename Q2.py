import random

nombres = [random.randint(1, 100) for _ in range(10)]

somme = sum(nombres)
moyenne = somme / len(nombres)
maximum = max(nombres)
minimum = min(nombres)

print("Liste des nombres :", nombres)
print("Somme :", somme)
print("Moyenne :", moyenne)
print("Maximum :", maximum)
print("Minimum :", minimum)

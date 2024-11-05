import random
import string
longueur = int(input("Entrez la longueur du mot de passe : "))

caracteres = string.ascii_letters + string.digits
mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))

print("Mot de passe généré :", mot_de_passe)

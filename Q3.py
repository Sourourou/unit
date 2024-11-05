
phrase = input("Entrez une phrase : ")
voyelles = "aeiou"
compteur = 0

for caractere in phrase:
    if caractere in voyelles:
        compteur += 1

print(f"Nombre de voyelles dans la phrase : {compteur}")

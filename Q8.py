
synonymes = {
    "sourourou": "srr",
    "sidi bouye": "SDB",
    "rapide": "vite",
    "content": "heureux",
    "intelligent": "brillant",
    "petit": "minuscule",
    "grand": "immense"
}

mot = input("Entrez un mot : ")


if mot in synonymes:
    print(f"Synonyme de '{mot}' :", synonymes[mot])
else:
    print("Aucun synonyme trouvé pour ce mot.")


annuaire = []


def ajouter_contact(nom, numero):
    contact = {"nom": nom, "numero": numero}
    annuaire.append(contact)

def afficher_contacts():
    if annuaire:
        for contact in annuaire:
            print(f"Nom: {contact['nom']}, Numéro: {contact['numero']}")
    else:
        print("Aucun contact dans l'annuaire.")

def supprimer_contact(nom):
    global annuaire
    annuaire = [contact for contact in annuaire if contact["nom"] != nom]
    
while True:
    print("\n--- Gestion de Contacts ---")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Supprimer un contact")
    print("4. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        nom = input("Entrez le nom : ")
        numero = input("Entrez le numéro : ")
        ajouter_contact(nom, numero)
        print("Contact ajouté.")

    elif choix == "2":
        afficher_contacts()

    elif choix == "3":
        nom = input("Entrez le nom du contact à supprimer : ")
        supprimer_contact(nom)
        print("Contact supprimé.")

    elif choix == "4":
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")

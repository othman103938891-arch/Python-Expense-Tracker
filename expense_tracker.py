expenses = []
def add_expense():
# Travail de l'etudiant A
    pass
def show_expenses():
# Travail de l'etudiant B
    pass
def show_total():
# Travail de l'etudiant B
    pass
def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        choice = input("Votre choix : ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
        if __name__ == "__main__":
            main()

expenses = []

def add_expense():
    description = input("Description : ")

    try:
        amount = float(input("Montant : "))
        if amount <= 0:
            print("Le montant doit etre superieur a zero.")
            return
    except ValueError:
        print("Veuillez entrer un montant valide.")
        return

    expenses.append({
        "description": description,
        "amount": amount
    })

    print("Depense ajoutee !")


def show_expenses():
    if not expenses:
        print("Aucune depense enregistree.")
        return

    print("\n===== LISTE DES DEPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - "
              f"{expense['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total : {total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
    choice = input("Expense number to delete: ")
    if not choice.isdigit():
        print("Invalid expense number.")
        return
    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")

def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Delete an expense")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Au revoir !")
            break
        elif choice == "5":
            delete_expense()

        else:
            print("Choix invalide. Veuillez choisir entre 1 et 4.")


if __name__ == "__main__":
    main()

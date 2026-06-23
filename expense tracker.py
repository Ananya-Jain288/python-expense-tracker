expenses = []

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n------ ALL EXPENSES ------")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} | {expense['category']} | ₹{expense['amount']}")

def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending = ₹{total}")

def average_expense():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = sum(expense["amount"] for expense in expenses)

    avg = total / len(expenses)

    print(f"Average Expense = ₹{avg:.2f}")

def highest_expense():
    if len(expenses) == 0:
        print("No expenses available.")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print("\nHighest Expense:")
    print(f"{highest['name']} | {highest['category']} | ₹{highest['amount']}")

def search_expense():
    keyword = input("Enter expense name to search: ").lower()

    found = False

    for expense in expenses:
        if keyword in expense["name"].lower():
            print(f"{expense['name']} | {expense['category']} | ₹{expense['amount']}")
            found = True

    if not found:
        print("Expense not found.")

def delete_expense():
    view_expenses()

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        removed = expenses.pop(index)

        print(f"{removed['name']} deleted successfully!")

    except:
        print("Invalid expense number.")

while True:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Average Expense")
    print("5. Highest Expense")
    print("6. Search Expense")
    print("7. Delete Expense")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        average_expense()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        search_expense()

    elif choice == "7":
        delete_expense()

    elif choice == "8":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

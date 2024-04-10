from datetime import datetime

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses_by_user = {}

    def add_expense(self, username, expense):
        if username not in self.expenses_by_user:
            self.expenses_by_user[username] = []
        self.expenses_by_user[username].append(expense)

    def get_expenses(self, username):
        return self.expenses_by_user.get(username, [])

    def get_total_expenses(self, username):
        return sum(expense.amount for expense in self.get_expenses(username))

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            date = datetime.now()  # Assuming current date for simplicity
            expense = Expense(category, amount, date)
            expense_tracker.add_expense(username, expense)
            print("Expense added successfully!")
        elif choice == '2':
            username = input("Enter your username: ")
            expenses = expense_tracker.get_expenses(username)
            if not expenses:
                print("No expenses found for the user.")
            else:
                print("Expenses for", username + ":")
                for expense in expenses:
                    print("Category:", expense.category +
                          ", Amount:", expense.amount +
                          ", Date:", expense.date.strftime("%d/%m/%Y"))
                print("Total expenses:", expense_tracker.get_total_expenses(username))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

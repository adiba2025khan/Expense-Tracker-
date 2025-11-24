import csv
import os

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self._load_expenses()

    def _load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        self.expenses.append({
                            "Date": row["Date"].strip(),
                            "Category": row["Category"].strip(),
                            "Amount": float(row["Amount"]),
                            "Description": row["Description"].strip()
                        })
                    except (ValueError, KeyError):
                        continue

    def _save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount", "Description"])
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow({
                    "Date": exp["Date"],
                    "Category": exp["Category"],
                    "Amount": f"{exp['Amount']:.2f}",
                    "Description": exp["Description"]
                })

    def add_expense(self, date, category, amount, description):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount! Expense not added.")
            return

        self.expenses.append({
            "Date": date.strip(),
            "Category": category.strip(),
            "Amount": amount,
            "Description": description.strip()
        })
        self._save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nDate       | Category       | Amount   | Description")
        print("-"*60)
        for exp in self.expenses:
            print(f"{exp['Date']:<10} | {exp['Category']:<13} | ₹{exp['Amount']:>7.2f} | {exp['Description']}")

    def total_expenses(self):
        total = sum(exp["Amount"] for exp in self.expenses)
        print(f"Total Expenses: ₹{total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            tracker.add_expense(date, category, amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
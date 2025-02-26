'''This program is the first version of the bank management system.
There are two classes Transaction  and Bank to manage the bank transactions.
'''
import json
class Transaction:
    # first function to initialize the class Transaction
    def __init__(self, title, amount, type, note):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note
    
    #sedcond function to disdplay the transcation
    def display(self):
        return f"Transaction:\nExpense:{self.title}\nAmount:{self.amount}\nType:{self.type}\nNote:{self.note}"

class Bank:
    #create a function called wallet to store the currency.

    def __init__(self):
        self.wallet = 0
    
    #creare a function to add the transaction to the wallet.
    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    #create a function to delete a transaction from the wallet.
    def del_transaction(self, title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"Transaction {title} has been removed."
            
            return f"tranaction {title} not found."
        
    #create a function to search a transaction in the wallet.
    def search_transaction(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() in trans.type.lower()]

        if not found:
            return f"Not found"
        
        return "\n.join ([transaction .display_info() for transaction in found])"
    
    #create a function to save the transaction to a JSON file

    def save_to_file(self, filename = "wallet.json"):
         data = [{'Expense': transaction.title, 'Amount': transaction.amout, 'Type': transaction.type, 'Note': 
                  transaction.note} for transaction in self.wallet]
         with open(filename, "w") as file:
             json.dump(data, file)

    #create a function to load the transacation from the JSON file in the form of the list.
    def load_from_file(self, filename = "wallet.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.wallet = [Transaction(trans['title'], trans['amount'], trans['type'], trans['note']) for trans in data]
        except FileNotFoundError:
            print("file not found.")

def main():
    wallet = Bank()

    while True:
        print("\n==== Personal Banking System ====")
        print("1. Add a transaction")
        print("2. Delete a transaction")
        print("3. Display all transactions")
        print("4. Search for a transaction")
        print("5. save transactions to a file")
        print("6. Load transactions from a file")
        print("7. Exit.")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the title of the transaction: ")
            amount = float(input("Enter the anount of the transaction: "))
            type = input("Enter the type of the transaction (Credit or Deposit): ")
            transaction = Transaction(title, amount, type)
            wallet.add_transaction(transaction)
            print("Transaction added successfully")

        elif choice == "2":
            title = input("Enter the title of the tranaction to delete: ")
            print(wallet.remove_transaction(title))
        
        elif choice == "3":
            print(wallet.display)

        elif choice == "4":
            query = input("Enter the search query: ")
            print(wallet.search_transaction(query))

        elif choice == "5":
            wallet.save_to_file()
            print("Transaction saved to file.")

        elif choice == "6":
            wallet.load_from_file()
            print("Transaction loaded from file.")
        
        elif choice == "7":
            print("Thank you for using the Personal Banking System.")
            break
        else:
            print("Invalid choice. Try again.")




if __name__ in "__main__":
    main()


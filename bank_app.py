
# account_state dictionary to hold all global data
account_state = {
    "account_counter": 1000,
    "accounts": {}
}

# Create Account
def create_account():
    name = input("Enter your name: ")
    opening_balance = float(input("Enter opening balance: "))
    account_state["account_counter"] += 1
    acc_number = account_state["account_counter"]
    account_state["accounts"][acc_number] = {
        "name": name,
        "balance": opening_balance
    }
    print(f"Account created! Your account number is {acc_number}\n")


# Deposit Money
def deposit_money():
    acc_number = int(input("Enter your account number: "))
    if acc_number in account_state["accounts"]:
        amount = float(input("Enter deposit amount: "))
        account_state["accounts"][acc_number]["balance"] += amount
        print("Deposit successful!\n")
    else:
        print("Account not found.\n")


# Withdraw Money
def withdraw_money():
    acc_number = int(input("Enter your account number: "))
    if acc_number in account_state["accounts"]:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= account_state["accounts"][acc_number]["balance"]:
            account_state["accounts"][acc_number]["balance"] -= amount
            print("Withdrawal successful!\n")
        else:
            print("Insufficient balance.\n")
    else:
        print("Account not found.\n")


# Check Balance
def check_balance():
    acc_number = int(input("Enter your account number: "))
    if acc_number in account_state["accounts"]:
        acc = account_state["accounts"][acc_number]
        print(f"Account Name: {acc['name']}")
        print(f"Balance: GHS {acc['balance']:.2f}\n")
    else:
        print("Account not found.\n")


#View All Accounts
def view_all_accounts():
    if not account_state["accounts"]:
        print("No accounts found.\n")
    else:
        print("All Bank Accounts:")
        for acc_number, acc in account_state["accounts"].items():
            print(f"Acc No: {acc_number} | Name: {acc['name']} | Balance: GHS {acc['balance']:.2f}")
        print()


# Main Menu Loop
def main():
    while True:
        print("==== Welcome to the Bank App ====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")

        choice = input("Select an option (1-6): ")
        print()

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            view_all_accounts()
        elif choice == '6':
            print("Goodbye! Thank you for using the Bank App.")
            break
        else:
            print("Invalid option. Try again.\n")


# Start the application
main()

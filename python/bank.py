class Bank:
    def __init__(self, Acc_no, Name, Acc_type, Balance):
        self.Acc_no = Acc_no
        self.Name = Name
        self.Acc_type = Acc_type
        self.Balance = Balance

    def deposit(self, Amount):
        if Amount > 0:
            self.Balance = self.Balance + Amount
            print("Successful deposit of", Amount)
            print("New balance =", self.Balance)
        else:
            print("INVALID")

    def withdraw(self, damount):
        if 0 < damount <= self.Balance:
            self.Balance = self.Balance - damount
            print("Withdrawn successfully", damount)
            print("New balance =", self.Balance)
        elif damount > self.Balance:
            print("Not possible to withdraw. Insufficient balance.")
        else:
            print("Invalid")

    def get_balance(self):
        print("Current balance =", self.Balance)

Account1 = Bank("101", "Malavika", "Savings", 15000)
while True:
    print("\n1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        Account1.get_balance()
    elif choice == '2':
        d_amount = int(input("Enter the amount to be deposited: "))
        Account1.deposit(d_amount)
    elif choice == '3':
        w_amount = int(input("Enter the amount to withdraw: "))
        Account1.withdraw(w_amount)
    elif choice == '4':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


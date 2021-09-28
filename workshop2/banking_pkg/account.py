def show_balance(balance):

   return balance
   


def deposit(balance):
    amount = input("Enter amount to deposit: ")
   
    balance = balance + float(amount)
   
    return balance 


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    balance = balance - float(amount)
    return balance 


def logout(name):
    print("Goodbye", name, "!")

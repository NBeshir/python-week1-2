from banking_pkg import account


def atm_menu():
    print("")
    print("          === Automated Teller Machine ===         \n ")
    name = input("Enter name to register: ")
    pin = input("Enter pin: ")
    balance = 0
    print(name + " has been registered with a starting balance of $" + str(balance))
    while True:
        print("\nLogin")
        name_to_validate = input("\nEnter name : ")
        pin_to_validate = input("\nEnter pin: ")
        if(name_to_validate == name and pin_to_validate == pin):
            print("\nLOGIN Successful!\n")
            break
        else:
            print("\nInvalid credentials!")

    while True:
        print(" \n         === Automated Teller Machine ===         \n ")
        print("User:", name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")

        print("------------------------------------------")

        option = input("Choose an option:")
        if option == "1":
            account.show_balance(balance)
            print("Current Balance:","$" + str(balance))

        elif option == "2":
            balance =   account.deposit(balance)
          
            print("Current balance:", "$" + str(balance))
          

        elif option == "3":
            balance = account.withdraw(balance)
            
            print("Current balance:", "$" + str(balance))
        elif option == "4":
            account.logout(name)
            break


atm_menu()

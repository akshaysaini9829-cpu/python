balance = 50000

pin = 1234

code = int(input("Enter your pin code"))
if code == pin:
    print("pin is correct!")

    while True:
        print("----ATM MENU----")
        print(" 1. check balance")
        print(" 2. withdraw money ")
        print(" 3.Deposit money ")
        print("4. exit")
         
        choice = int(input("Enter your choice"))

# check balance 
        if choice == 1:
            print("your balance is:",balance)

# withdraw money
        elif choice == 2:
            amount = int(input("Enter your ammount"))

            if amount <= 0:
                print("amount is negative")

            elif amount > balance:
                print("insuffiecient balance!")

            else:
                balance = balance - amount

                print("remaining balance:",balance)

     # 3. deposit balance 

        elif choice == 3:
            amount = float(input("Enter deposit amount"))

            if amount <= 0:
                print("amount is negative")
            else:

                balance = balance + amount
                print("updated balance",balance)


    # Exit
        elif choice == 4:
            print("thanks you")
            break

        else:
            print("invalid choice")

else:
    print("pin is incorrect") 
    print("please try again")           

    







        

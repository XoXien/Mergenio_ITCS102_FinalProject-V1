# Mini Bank Simulator
has_account = False
running = True
import os
bal = 0

def deposit_money():
    global bal
    os.system('cls')
    print("------------------------------------------")
    print("--- Welcome to TheBank Deposit Service ---")
    print("------------------------------------------")
    amount = eval(input("How much would you like to deposit?"))

    onethou = amount // 1000
    onethou2 = amount % 1000
    
    fiveh = onethou2 // 500
    fiveh2 = onethou2 % 500
    
    twoh = fiveh2 // 200
    twoh2 = fiveh2 % 200
    
    oneh = twoh2 // 100
    oneh2 = twoh2 % 100

    fifty = oneh2 // 50
    fifty2 = oneh2 % 50
    
    twenty = fifty2 // 20
    twenty2 = fifty2 % 20
    
    ten = twenty2 // 10
    ten2 = twenty2 % 10
    
    five = ten2 // 5
    five2 = ten2 % 5
    
    one = five2 // 1
    one2 = five2 % 1

    os.system('cls')
    print("Filipino denominations of the amount you would like to deposit is as follows:")
    print(f"| ₱1000 = {onethou} |")
    print(f"| ₱500  = {fiveh} |")
    print(f"| ₱200  = {twoh} |")
    print(f"| ₱100  = {oneh} |")
    print(f"| ₱50   = {fifty} |")
    print(f"| ₱20   = {twenty} |")
    print(f"| ₱10   = {ten} |")
    print(f"| ₱5    = {five} |")
    print(f"| ₱1    = {one} |")
    print(f"Amount entered: {amount}")

    choice1 = input("Would you like to deposit the amount? (Y or N)")
    if choice1.lower() == "y":
        os.system('cls')
        bal += amount
        print("-----------------------------------------")
        print(f"--- Successfully deposited ₱{amount} ---")
        print("-----------------------------------------")
        bla = input("Enter any input to continue:")
        return bal
    elif choice1.lower() == "n":
        os.system('cls')
        print("Deposit session has ended:")
        print()
        return bal

def check_balance():
    print("------------------------------------------------")
    print("--- Welcome to TheBank Check Balance Service ---")
    print("------------------------------------------------")
    print(f"--- Your total balance is ₱{bal} ---")
    bla = input("Enter any input to continue:")

def withdraw_money():
    global bal
    os.system('cls')
    print("-------------------------------------------")
    print("--- Welcome to TheBank Withdraw Service ---")
    print("-------------------------------------------")
    amount = eval(input("How much would you like to withdraw? "))
    if amount >= bal:
        print("Withdraw must not be greater than the available balance.")
        print(f"Amount entered: {amount}")
        print(f"Current account balance: {bal}")
        bla = input("Enter any input to continue.")
    elif amount == bal or amount <= bal:
        bal -= amount
        os.system('cls')
        print(f"{amount} has been withdrawn, current balance is now {bal}.")
        bla = input("Enter any input to continue: ")
        return bal
    else:
        print("Invalid input.")
        print()

while running == True:
    print("-----------------------------------")
    print("--- Welcome to TheBank Services ---")
    print("-----------------------------------")
    if has_account == False:
        print("You need an account to use the system")
        sign_in = input("Would you like to create an account? (Y or N) : ")
        if sign_in.lower() == "y":
            os.system('cls')
            print("----------------------")
            print("--- Create Account ---")
            print()
            name = input("Please enter your name: ")
            password = input("Create your own password: ")
            pass_confirm = input("Re-enter your password: ")
            if pass_confirm == password :
                print()
                print("---Account successfully created---")
                print("----------------------------------")
                has_account = True
                bla = input("Enter any input to continue:")
                os.system('cls')
        elif sign_in.lower() == "n":
            print("Thank you for using our system!")
            running = False
            break

    elif has_account == True:
        while running == True:
    
            print("Please Input Your Credential to Access your TheBank Account")
            whatname = input("Enter your Name: ")
            if whatname == name:
                whatpass = input("Enter your Password: ")
                if whatpass == password:
                    while running == True:
                        os.system('cls')
                        print("-----------------------------------------------")
                        print("--- Welcome to TheBank Services (Main Menu) ---")
                        print("-----------------------------------------------")
                        print(f"Hi {name}! What would you like to do for today?")
                        print("---1. Check balance ---")
                        print("---2. Deposit money ---")
                        print("---3. Withdraw money---")
                        print("---4. End program   ---")
                        choice = input("Please Input the Service Number (1,2,3,4): ")
                        os.system('cls')
                        if choice == "1":
                            check_balance()
                        elif choice == "2":
                            deposit_money()
                        elif choice == "3":
                            withdraw_money()
                        elif choice == "4":
                            print("-----------------------------------------")
                            print("--- Thank you for using our services! ---")
                            print("-----------------------------------------")
                            running = False
                            break
                        os.system('cls')
                elif whatpass != password:
            
                    print("--- Incorrect password--- ")
                    bla = input("Enter any input to continue: ")
            elif whatname != name:
        
                print("--- Account doesn't exist ---")
                print("--- Please Ensure you enter correct Account Name ---")
                bla = input("Enter any input to continue.")
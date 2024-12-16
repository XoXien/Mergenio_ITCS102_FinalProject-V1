import os
import sys
import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

# Loading Animation
# Credits:https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running with some modification  
class Loader:
    def __init__(self, desc="Loading...", timeout=0.1):
        self.desc = desc
        self.timeout = timeout
        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def start(self):
        self._thread.start()

    def stop(self):
        self.done = True
        print("\r" + " " * get_terminal_size().columns, end="", flush=True)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()
# Loading Trigger
def animation():
    with Loader("Loading Please Wait! ..."):
        for _ in range(10):
            sleep(0.25)
    with Loader("Initializing all line of codes..."):
        for _ in range(10):
            sleep(0.25)
    os.system('cls')

def animation_2():
    with Loader("Loading Please Wait! ..."):
        for _ in range(10):
            sleep(0.25)
    os.system('cls')

# Progressbar Loading
# Credits: https://stackoverflow.com/questions/3160699/python-progress-bar with some modification  
def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size * j / count)
        elapsed = time.time() - start
        print(f"{prefix}[{'■' * x}{'.' * (size - x)}] {j}/{count} ", end='\r', file=out, flush=True)
    show(0.1)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)

# Progressbar Trigger
def main():
    for item in progressbar(range(100), prefix="Progress:", size=40):
        time.sleep(0.02)
    os.system('cls')
    
# Printing Functions
def simple_printing():
    print("---------------------------------------\n")
    print("This is an Example of Simple printing\n")
    print("Input:")
    print('print("Hello World!")')
    print('print("Bonjour!")')
    print('print("Ni Hao")')
    print()
    print("Output:")
    print("Hello World!")
    print("Bonjour!")
    print("Ni Hao!\n")
    print("---------------------------------------")
    clear= input("Enter any character:")

def string_formatting():
    print("-----------------------------------------------------\n")
    print("This is an Example of Simple printing\n")
    print("Input:")
    print("name = input('Enter your name: ')")
    print("age = input('Enter your age: ')")
    print("print(f'Hello {name}, you are {age} years old.')")
    print()
    print("Output:")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old.")
    print("-----------------------------------------------------")
    clear= input("Enter any character:")

# Variables Functions
def concatenation_with_variables():
    print("-----------------------------------------------------\n")
    print("Input:")
    print('first_name = input("Enter your first name: ")')
    print('last_name = input("Enter your last name: ")')
    print('full_name = first_name + " " + last_name')
    print('print("Full Name: " + full_name)')
    print()
    print("Output:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    print("Full Name: " + full_name)
    print("-----------------------------------------------------")
    clear= input("Enter any character:")

def tuple_example():
    print("---------------------------------\n")
    print("Input:")
    print("my_tuple = (1, 2, 3, 4)")
    print('print(f"Tuple: {my_tuple}")')
    print()
    print("Output:")
    my_tuple = (1, 2, 3, 4)
    print(f"Tuple: {my_tuple}")
    print("---------------------------------2")
    clear= input("Enter any character:")

# Conditional Statements Functions
def conditional_statement_simple():
    print("---------------------------------\n")
    print("Input:")
    print('x = int(input("Enter a number: "))')
    print('if x == 10:')
    print('    print("You entered 10!")')
    print('else:')
    print('    print("You did not enter 10.")')
    print()
    print("Output:")
    x = int(input("Enter a number: "))
    if x == 10:
        print("You entered 10!")
    else:
        print("You did not enter 10.")
    print("---------------------------------\n")
    clear= input("Enter any character:")

def conditional_statement_logical():
    print("---------------------------------\n")
    print("Inputs:")
    print("    print(\"If 2 input are not the same '!='\")")
    print("    x = eval(input(\"Please input a number: \"))")
    print("    y = eval(input(\"Please input a number: \"))")
    print("    if x != y:")
    print("        print(True)")
    print("    else:")
    print("        print(False)")
    print("    print()")
 
    print("    print(\"If 1 input is less than to the other one '<'\")")
    print("    x = eval(input(\"Please input a number: \"))")
    print("    y = eval(input(\"Please input a number: \"))")
    print("    if x < y:")
    print("        print(True)")
    print("    else:")
    print("        print(False)")
    print("    print()")

    print("    print(\"If 1 input is less than or equal to the other one '<='\")")
    print("    x = eval(input(\"Please input a number: \"))")
    print("    y = eval(input(\"Please input a number: \"))")
    print("    if x <= y:")
    print("        print(True)")
    print("    else:")
    print("        print(False)")
    print("    print()")

    print("    print(\"If 1 input is greater than to the other one '>'\")")
    print("    x = eval(input(\"Please input a number: \"))")
    print("    y = eval(input(\"Please input a number: \"))")
    print("    if x > y:")
    print("        print(True)")
    print("    else:")
    print("        print(False)")
    print("    print()")

    print("    print(\"If 1 input is greater than or equal to the other one '>='\")")
    print("    x = eval(input(\"Please input a number: \"))")
    print("    y = eval(input(\"Please input a number: \"))")
    print("    if x >= y:")
    print("        print(True)")
    print("    else:")
    print("        print(False)")
    print("    print()")
    print()
    print("Outputs")
    # Not Equals: x != y
    print("If 2 input are not the same '!='")

    x = eval(input("Please input a number: "))
    y = eval(input("Please input a number: "))

    if x != y:
        print(True)
    else:
        print(False)
    print()

    # Less than: x < y
    print("If 1 input is less than to the other one '<'")

    x = eval(input("Please input a number: "))
    y = eval(input("Please input a number: "))

    if x < y:
        print(True)
    else:
        print(False)
    print()

    # Less than or equal to: x <= y
    print("If 1 input is less than or equal to the other one '<='")

    x = eval(input("Please input a number: "))
    y = eval(input("Please input a number: "))

    if x <= y:
        print(True)
    else:
        print(False)
    print()

    # Greater than: x > y
    print("If 1 input is greater than to the other one '>'")

    x = eval(input("Please input a number: "))
    y = eval(input("Please input a number: "))

    if x > y:
        print(True)
    else:
        print(False)
    print()
    # Greater than or equal to: x >= y
    print("If 1 input is greater than or equal to the other one '>='")

    x = eval(input("Please input a number: "))
    y = eval(input("Please input a number: "))

    if x >= y:
        print(True)
    else:
        print(False)
    print()
    print("---------------------------------")
    clear= input("Enter any character:")

def multiple_conditions():
    print("---------------------------------\n")
    print("Input:")
    print('password = "AlphaTest"')
    print('mypassword = input("Enter your password: ")')
    print()
    print('if password.lower() == mypassword.lower():')
    print('    print("Good Job!, You provided your password correctly.")')
    print('    print("Welcome!")')
    print()
    print('elif mypassword == "1":')
    print('    print("Nice!, You unlocked your account with your alternate password.")')
    print('    print("Welcome!")')
    print()
    print('else:')
    print('    print("Access Denied")')
    print()
    print("Output:")
    password = "AlphaTest"
    mypassword = input("Enter your password: ")
    
    if password.lower() == mypassword.lower():
        print("Good Job!, You provided your password correctly. ")
        print("Welcome!")

    elif mypassword == "1":
        print("Nice!, You unlock your account with your alternate password") 
        print("Welcome!")

    else:
        print("Access Denied  ")
    print("---------------------------------")
    clear= input("Enter any character:")

def nested_conditionals():
    print("---------------------------------\n")
    print("Input:")
    print('x = eval(input("Enter a number: "))')
    print('if x >= 0:')
    print('    if x == 0:')
    print('        print("You entered zero.")')
    print('    else:')
    print('        print(f"You entered a positive number: {x}")')
    print('else:')
    print('    print(f"You entered a negative number: {x}")')
    print()
    print("Output:")
    x = eval(input("Enter a number: "))
    if x >= 0:
        if x == 0:
            print("You entered zero.")
        else:
            print(f"You entered a positive number: {x}")
    else:
        print(f"You entered a negative number: {x}")
    print("---------------------------------")
    clear= input("Enter any character:")

# Looping Functions
def for_loop():
    print("---------------------------------\n")
    print("Input:")
    print('num = eval(input("Enter the column number:  "))')
    print('for x in range(1, 11):')
    print('    for y in range(1, num + 1):')
    print('        print(f"{x}*{y}={x*y}", end="\\t")')
    print('    print()')
    print()
    print("Output:")
    num = eval(input("Enter the column number:  "))
    for x in range(1,11):
        for y in range(1,num+1):
            print(f"{x}*{y}={x*y}",end="\t")
        print()
    print("---------------------------------")
    clear= input("Enter any character:")

def while_loop():
    print("---------------------------------\n")
    print("Input:")
    print('Tuloy = True')
    print('sum = 0')
    print('while Tuloy:')
    print('    num = eval(input("Enter any number --->  "))')
    print()
    print('    if num == 0:')
    print('        print("LOOP STOPPED")')
    print('        print(f"The sum of all the numbers given is {sum}")')
    print('        break')
    print('        tuloy = False')
    print('    else:')
    print('        sum += num')
    print('        continue')
    print()
    print("Output:")
    Tuloy = True 
    sum = 0
    while Tuloy == True:
        num = eval(input("Enter any number --->  "))

        if num == 0:
            print("LOOP STOPPED")
            print(f"The sum of all the numbers given is {sum}")
            break
            tuloy = False 
        else:
            sum += num 
            continue
    print("---------------------------------")
    clear= input("Enter any character:")
    
# Functions
def function_example():
    print("---------------------------------\n")
    print("Input:")
    print('def greet(name):')
    print('    print(f"Hello {name}!")')
    print()
    print('name = input("Enter your name: ")')
    print('greet(name)')
    print()
    print("Output:")
    def greet(name):
        print(f"Hello {name}!")
    name = input("Enter your name: ")
    greet(name)
    print("---------------------------------")
    clear= input("Enter any character:")

# List Functions
def list_example():
    print("---------------------------------\n")
    print("Input:")
    print('fruits=["cherry","banana","apple",]')
    print('print(fruits)')
    print()
    print("Output:")
    fruits=["cherry","banana","apple",]
    print(fruits)
    print("---------------------------------")
    clear= input("Enter any character:")

def editing_list():
    print("---------------------------------\n")
    print("Input:")
    print('fruits = ["apple", "grapes", "banana", "pineapple", "watermelon"]')
    print()
    print('print("Accessing an item")')
    print('print(f"My favorite fruit is {fruits[1]}")')
    print()
    print('print("Add an item to the end of the list")')
    print('fruits.append("longgan")')
    print('print(f"Updated List: {fruits}")')
    print()
    print('print("Inserting an item on specific index")')
    print('fruits.insert(3,"guyabano")')
    print('print(f"Updated List: {fruits}")')
    print()
    print('print("Change item or value")')
    print('fruits[0] = "kiwi"')
    print('print(f"Updated List: {fruits}")')
    print()
    print('print("Remove item on list")')
    print('fruits.remove("banana")')
    print('print(f"Updated List: {fruits}")')
    print()
    print('print("To determine how many items a list has")')
    print('print(len(fruits))')
    print()
    print("Output:")
    fruits=["apple","grapes","banana","pineapple","watermelon"]
    print("Accesing an item")
    print(f"My favorite fruit is {fruits[1]}")
    print()

    print("Add an item to the end of the list")
    fruits.append("longgan")
    print(f"Updated List: {fruits}")
    print()

    print("Inserting an item on specific index")
    fruits.insert(3,"guyabano")
    print(f"Updated List: {fruits}")
    print()

    print("Change item or value")
    fruits[0] = "kiwi"
    print(f"Updated List: {fruits}")
    print()

    ("Remove item on list")
    fruits.remove("banana")
    print(f"Updated List: {fruits}")
    print()

    print("To determine how many items a list has")
    print(len(fruits))
    print("---------------------------------")
    clear= input("Enter any character:")

# Math Functions
def arithmetic_operators():
    print("---------------------------------\n")
    print("Input:")
    print('a = eval(input("Please Enter a number: "))')
    print('b = eval(input("Please Enter a number: "))')
    print()
    print('print(f"Addition: {a + b}")')
    print('print(f"Subtraction: {a - b}")')
    print('print(f"Multiplication: {a * b}")')
    print('print(f"Division: {a / b}")')
    print('print(f"Modulus: {a % b}")')
    print('print(f"Exponentiation: {a ** b}")')
    print()
    print("Output:")
    a = eval(input("Please Enter a number: "))
    b = eval(input("Please Enter a number: "))
    print()
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Modulus: {a % b}")
    print(f"Exponentiation: {a ** b}")
    print("---------------------------------")
    clear= input("Enter any character:")

def temperature():
    print("---------------------------------\n")
    print("Input:")
    print('F = eval(input("Enter Temperature in FARENHEIT: "))')
    print('C = ((F - 32)*5)/9')
    print('round(C,2)')
    print('print(f"{F} degrees in Farenheit converted to Celsius is {C}")')
    print('C = eval(input("Enter Temperature in CELSIUS: "))')
    print('F = (C * 9/5) + 32')
    print('print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")')
    print()
    print("Output:")
    F = eval(input("Enter Temperature in FARENHEIT: "))
    C = ((F - 32)*5)/9
    round(C,2)

    print(f"{F} degrees in Farenheit converted to Celsius is {C}")

    C = eval(input("Enter Temperature in CELSIUS: "))
    F = (C * 9/5) + 32

    print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")
    print("---------------------------------")
    clear= input("Enter any character:")
#Calculator
def calculator_temperature():
    print("-------------------------------------")
    print("\tSimple Calculator")
    print(" 1. Temperature Conversion")
    print(" 2. Arithmetic Operations")
    print("-------------------------------------")
    choice = input("Enter your choice: ")
    os.system('cls')

    if choice == '1':
        print("-------------------------------------")
        print("\tTemperature Conversion")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("-------------------------------------")
        temp_choice = input("Enter your choice: ")
        
        if temp_choice == '1':
            print("---------------------------------------------")
            F = eval(input("Enter Temperature in Fahrenheit: "))
            C = ((F - 32) * 5) / 9
            print(f"{F} degrees Fahrenheit is {round(C, 2)} degrees Celsius.")
            print("-------------------------------------")
            clear= input("Enter any character:")
            os.system('cls')
    
        elif temp_choice == '2':
            print("---------------------------------------------")
            C = eval(input("Enter Temperature in Celsius: "))  
            F = (C * 9/5) + 32
            print(f"{C} degrees Celsius is {round(F, 2)} degrees Fahrenheit.")
            print("-------------------------------------")
            clear= input("Enter any character:")
            os.system('cls')
    
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    elif choice == '2':
        print("-------------------------------------")
        print("\tArithmetic Operations")
        print(" 1. Add")
        print(" 2. Subtract")
        print(" 3. Multiply")
        print(" 4. Divide")
        print("-------------------------------------")
        operation_choice = input("Enter your choice: ")

        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))

        if operation_choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            clear= input("Enter any character:")
            os.system('cls')
    
        elif operation_choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            clear= input("Enter any character:")
            os.system('cls')
    
        elif operation_choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            clear= input("Enter any character:")
            os.system('cls')
    
        elif operation_choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                clear= input("Enter any character:")
                os.system('cls')
            else:
                print("Error! Division by zero is not allowed.")
                clear= input("Enter any character:")
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
            clear= input("Enter any character:")
    else:
        print("Invalid input! Please enter 1 or 2.")
        clear= input("Enter any character:")

# MultiTable
def multi_table():
    print("---------------------------------\n")
    print("Input:")
    print('num = eval(input("Enter a number:  "))')
    print('for x in range(1,11):')
    print('    for y in range(1,num+1):')
    print('        print(f"{x}*{y}={x*y}",end="\t")')
    print('    print()')
    print()
    print("Output:")
    num = eval(input("Enter a number:  "))
    for x in range(1,11):
        for y in range(1,num+1):
            print(f"{x}*{y}={x*y}",end="\t")
        print()
    print("---------------------------------")
    clear= input("Enter any character:")

# Other Functions
def help_section():
    print("-------------------------------------")
    print("\t---Help Function ---")
    print("The help() function is a built-in function \nthat provides interactive help about Python \nobjects, such as modules, functions, classes, \nand more. It can be used in several ways to get \ninformation about various aspects of Python.")
    print("To Edit or make a help you need to put triple qoutes")
    print("-------------------------------------")
    clear= input("Enter any character:")
    os.system('cls')

def comments_section():
    print("-------------------------------------")
    print("\t--- Comments ---")
    print("Comments are used to add notes or \nexplanations within the code. These notes \nare ignored by the Python interpreter during \nexecution, meaning they do not affect the \nfunctionality of the program. Comments are \nuseful for explaining what the code does, \nmaking it easier to understand and maintain, \nespecially in larger projects. They start with #.")
    print("-------------------------------------")
    clear= input("Enter any character:")
    os.system('cls')
# Shapes
def box():
    print("---------------------------------\n")
    print("Input:")
    print('for x in range(1,11):')
    print('    print(end="\t")')
    print('    for y in range(1,11):')
    print('        print("*",end="")')
    print('    print()')
    print()
    print("Output:")
    for x in range(1,11):
        print(end="\t")
        for y in range(1,11):
            print("*",end="")
        print()
    print("---------------------------------")
    clear= input("Enter any character:")
    
def diamond():
    print("---------------------------------\n")
    print("Input:")
    print('for x in range(7,0,-1):')
    print('    for y in range(1,x+1):')
    print('        print(" ",end=" ")')
    print('    for z in range(6,x,-1):')
    print('        print("*",end=" ")')
    print('    for q in range(7,x,-1):')
    print('        print("*",end=" ")')
    print('    print()')

    print('for a in range(1,6):')
    print('    for b in range(0,a + 1):')
    print('        print(" ",end=" ")')
    print('    for c in range(5,a,-1):')
    print('        print("*",end=" ")')
    print('    for d in range(6,a,-1):')
    print('        print("*",end=" ")')
    print()
    print("Output:")
    for x in range(7,0,-1):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        for q in range(7,x,-1):
            print("*",end=" ")
        print()

    for a in range(1,6):
        for b in range(0,a + 1):
            print(" ",end=" ")
        for c in range(5,a,-1):
            print("*",end=" ")
        for d in range(6,a,-1):
            print("*",end=" ")
        print() 
    print("---------------------------------")
    clear= input("Enter any character:")

def right_pyramid_whileloop():
    print("---------------------------------\n")
    print("Input:")
    print('repeat = True')  
    print('nt = 0')  

    print('while repeat:') 
    print('var = input("Do you wish to add more triangles? (yes/no): ")')

    print('    if var.lower() == "no":') 
    print('        print("LOOP HAS BEEN STOPPED")')
    print('        repeat = False')  
    print('        break')  

    print('    elif var.lower() == "yes":') 
    print('        nt += 1') 
    print('        for x in range(1, 7):') 
    print('            for z in range(1, nt + 1):')
    print('                for y in range(1, x + 1):') 
    print('                    print("*", end=" ")')
    print('                for a in range(7, x, -1):') 
    print('                    print(" ", end=" ")')
    print('                print(end=" ")')  
    print('            print()')  

    print('    else:')
    print('        print("Invalid Input")')  
    print()
    print("Output:")
    repeat = True  
    nt = 0  

    while repeat:  
        var = input("Do you wish to add more triangles? (yes/no): ")

        if var.lower() == "no": 
            os.system('cls')
            print("LOOP HAS BEEN STOPPED")
            repeat = False  
            break  

        elif var.lower() == "yes":  
            os.system('cls')
            nt += 1  
            for x in range(1, 7):  
                for z in range(1, nt + 1):  
                    for y in range(1, x + 1):  
                        print("*", end=" ")
                    for a in range(7, x, -1):  
                        print(" ", end=" ")
                    print(end=" ")  
                print()  

        else:
            print("Invalid Input") 

    print("---------------------------------")
    clear= input("Enter any character:")
        
# Main Menu
def main_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Main Menu ---\n")
        print("1. Printing")
        print("2. Variables")
        print("3. Conditional Statements")
        print("4. Looping Statements")
        print("5. Functions")
        print("6. List")
        print("7. Others")
        print("0. Exit")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            animation_2()
            os.system('cls')
            printing_menu()
        elif choice == '2':
            animation_2()
            os.system('cls')
            variables_menu()
        elif choice == '3':
            animation_2()
            os.system('cls')
            conditional_statements_menu()
        elif choice == '4':
            animation_2()
            os.system('cls')
            looping_statements_menu()
        elif choice == '5':
            animation_2()
            os.system('cls')
            functions_menu()
        elif choice == '6':
            animation_2()
            os.system('cls')
            list_menu()
        elif choice == '7':
            animation_2()
            os.system('cls')
            others_menu()
        elif choice == '0':
            os.system('cls')
            main()
            print("-----------------------------------------------------")
            print("Thank You for using the system hope you learned something!")
            print("-----------------------------------------------------")
            break
        else:
            print("Invalid choice, try again.")

# Submenus
def printing_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Printing Menu ---")
        print("The print() function is used to display output to \nthe console or standard output device.It takes one \nor more objects (such as strings, numbers, or variables) \nas arguments and converts them into a human-readable form.")
        print("-----------------------")
        print(" 1. Simple Printing ")
        print(" 2. String Formatting")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")
        print()

        if choice == '1':
            simple_printing()
            os.system('cls')
        elif choice == '2':
            string_formatting()
            os.system('cls')
        elif choice == '0':
            animation_2()
            os.system('cls')
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def variables_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Variables Menu ---")
        print("A variable is a name that is used to refer to a value \nstored in memory. You can think of a variable as a container \nfor storing data values. Variables allow you to store, modify,\nand access data throughout your program.")
        print("----------------------------------")
        print(" 1. Concatenation with Variables")
        print(" 2. Tuple")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            concatenation_with_variables()
            os.system('cls')
        elif choice == '2':
            tuple_example()
            os.system('cls')
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def conditional_statements_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t--- Conditional Statements Menu ---")
        print("A conditional statement allows you to execute a block \nof code based on whether a condition is true or false. \nThe most common conditional statements are if, else, and \nelif.")
        print("----------------------------------")
        print(" 1. Simple using == and If/Else")
        print(" 2. Logical Conditions")
        print(" 3. Multiple Conditions")
        print(" 4. Nested Conditionals")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            conditional_statement_simple()
            os.system('cls')
        elif choice == '2':
            conditional_statement_logical()
            os.system('cls')
        elif choice == '3':
            multiple_conditions()
            os.system('cls')
        elif choice == '4':
            nested_conditionals()
            os.system('cls')
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def looping_statements_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t--- Looping Statements Menu ---")
        print("A loop statement in Python is used to execute a block \nof code repeatedly as long as a certain condition is met. \nLoops are useful when you need to perform repetitive tasks, \niterate over a sequence, or repeatedly check a condition.")
        print("-------------------------")
        print(" 1. For Loop")
        print(" 2. While Loop")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            for_loop()
            os.system('cls')
        elif choice == '2':
            while_loop()
            os.system('cls')
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def functions_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Functions Menu ---")
        print("A function in Python is a block of reusable code that \nperforms a specific task. Functions allow you to organize \nyour code into logical sections and avoid repetition. \nThey can take input (parameters), execute a series of \nstatements, and return output (a value).")
        print("-------------------------")
        print(" 1. Function Example")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            function_example()
            os.system('cls')
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def list_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- List Menu ---")
        print("A list in Python is a mutable (changeable) collection \ndata type that holds an ordered sequence of elements. \nLists can store items of different data types, such as \nnumbers, strings, or even other lists.")
        print("-------------------------")
        print(" 1. List Example")
        print(" 2. Editing List")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")

        if choice == '1':
            list_example()
            os.system('cls')
        elif choice == '2':
            editing_list()
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def shape_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Shape Menu ---")
        print("This Menu is all about the shape me and my classmates learned using while and for loop")
        print("--------------------------------------")
        print(" 1. Box (*)")
        print(" 2. Diamond(*)")
        print(" 3. Right Pyramid using While Loop")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            box()
            os.system('cls')
        elif choice == "2":
            diamond()
            os.system('cls')
        elif choice == "3":
            right_pyramid_whileloop()
            os.system('cls')
        elif choice == "0":
            animation_2()
            break
        else:
            print("Invalid choice. Please try again.")

def others_menu():
    while True:
        print("-----------------------------------------------------")
        print("\t\t--- Others Menu ---")
        print("This menu is all about my favorite Activities and Code. \nThis Menu include the other topic that I learned in ")
        print("--------------------------------------")
        print(" 1. Math - Arithmetic Operators")
        print(" 2. Temperature")
        print(" 3  Calculator with Temperature")
        print(" 4. Help")
        print(" 5. Comments")
        print(" 6. Multiplication Table")
        print(" 7. Shapes")
        print(" 0. Back To Main Menu")
        print("-----------------------------------------------------")
        print("")
        choice = input("Select an option: ")
        
        if choice == '1':
            arithmetic_operators()
            os.system('cls')
        elif choice == '2':
            temperature()
            os.system('cls')
        elif choice == '3':
            calculator_temperature()
            os.system('cls')    
        elif choice == '4':
            help_section()
            os.system('cls')
        elif choice == '5':
            comments_section()
            os.system('cls')
        elif choice == '6':
            multi_table()
            os.system('cls')  
        elif choice == '7':
            shape_menu()
            os.system('cls')        
        elif choice == '0':
            animation_2()
            break
        else:
            print("Invalid choice, try again.")
            clear= input("Enter any character:")
            os.system('cls')

def create_account():
    usernames = []
    passwords = []
    print("--------------------------------------------------")
    print("\t\t--- Account Creation --- ")
    username = input("Enter your desired username: ")
    if username in usernames:
        print("Username already exists. Please try a different username.")
        return usernames, passwords 
    password = input("Enter your desired password: ")
    print("--------------------------------------------------")
    
    usernames.append(username)
    passwords.append(password)
    main()
    print("--------------------------------------------------")
    print(f"Account created successfully for {username}!")

    return usernames, passwords

def login(usernames, passwords):
    print("--------------------------------------------------")
    print("\t\t-- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("--------------------------------------------------")
    
    if username in usernames:
        index = usernames.index(username) 
        if passwords[index] == password:
            main()
            print("--------------------------------------------------")
            print(f"Login Successfully, Welcome {username}!")
            print("--------------------------------------------------")
            clear= input("Enter any character:")
            os.system('cls')
            main_menu()
        else:
            print("Invalid username or password.")

usernames = []
passwords = []
main()
print(f"Starting Program Please Wait ")
animation()
print("--------------------------------------------------")
print("  Welcome To Mergenio ITCS102 Compilation ")
print("--------------------------------------------------")
create_account_choice = input("Do you want to create a new account? (yes/no): ")
print("--------------------------------------------------")
os.system('cls')

if create_account_choice.lower() == 'yes':
    usernames, passwords = create_account()
print("--------------------------------------------------")
login_choice = input("Do you want to log in? (yes/no): ")
print("--------------------------------------------------")

os.system('cls')

if login_choice.lower() == 'yes':
    login(usernames, passwords)
else:
    main()
    print("--------------------------------------------------")
    print("Thank you for using my system!")
    print("--------------------------------------------------")
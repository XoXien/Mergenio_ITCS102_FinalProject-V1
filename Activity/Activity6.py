#Decision structures/Conditional statements 

# Equals: x == y
print("If 2 input are the same '=='")
x = eval(input("Please input a number: "))
y = eval(input("Please input a number: "))

if x == y:
    print(True)
else:
    print(False)
print()

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

#Example with Elif  
password = "AlphaTest"


mypassword = input("Enter your password: ")

#Used to check a condition, and execute it if the condition holds true
if password.lower() == mypassword.lower():
    print("Good Job!, You provided your password correctly. ")
    print("Welcome!")

#If the previous conditions were not true, then try this condition
elif mypassword == "1":
    print("Nice!, You unlock your account with your alternate password") 
    print("Welcome!")

#Used in conditional statements (if statements), and decides what to do if the condition is False.
else:
    print("Access Denied  ")

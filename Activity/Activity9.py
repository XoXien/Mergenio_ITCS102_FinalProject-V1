# Factorial in for loop
# The user will input a number then this system will automatically calculate its Factorialr 
num = eval(input("Enter any number: "))
factorial = 1 

for x in range(num,0,-1):
    factorial *= x
print(f"The factorial of {num} is {factorial}")
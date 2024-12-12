#String Formatting
#The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. 
# Format: print(f"Hi Mr./Ms.{user}")

name = input("Enter your name: ")
print()
age = eval(input("Enter your age: "))
print()
address = input("Enter your home address: ")
print()

#Example without String Formatting
print("Hi" + name + "from" + address + "and" + age + "years  old")
#Example with String Formatting
print(f"Hi {name}, from {address} and {age} years  old")
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data
# The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

fruits=["apple","grapes","banana","pineapple","watermelon"]
print(fruits)
print()
#         0         1         2          3          4
fruits=["apple","grapes","banana","pineapple","watermelon"]

# Accesing an item
print(f"My favorite fruit is {fruits[1]}")
print()

# Add an item to the end of the list
fruits.append("longgan")
print(fruits)
print()

# Inserting an item on specific index
fruits.insert(3,"guyabano")
print(fruits)
print()

#Change item or value
fruits[0] = "kiwi"
print(fruits)
print()

#Remove item on list
fruits.remove("banana")
print(fruits)
print()

#To determine how many items a list has
print(len(fruits))

#  A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Its format is "For x in range(start, stop, step)

sum = 0
odd = 0 
even = 0

for x in range(1,11):
    num = eval(input(f"Input# {x}: "))
    sum += num 
    if num % 2 == 0:
        even += num
    else:
        odd += num
        
print(f"The sum of all numbers are: {sum}")
print(f"The sum of all even numbers are: {even}")
print(f"The sum of all odd numbers are: {odd}")
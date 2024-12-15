#Odd and Even in for loop
sum = 0
even = 0
odd = 0

for x in range (1,11):
    num = eval(input(f"Enter a #{x} number: "))
    sum += num

    if num % 2 == 0:
        even += num
    else :
        odd += num

print()

print(f"The SUM of all the number you enter is {sum}")
print(f"The SUM of all EVEN number you enter is {even}")
print(f"The SUM of all ODD number you enter is {odd}")
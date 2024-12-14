#Box Asterisk (*) using For Loop
#In every print() there is a \n on the end
#To access it you need to ,end=" " at the end you can put various escape sequence like in the code below 

for x in range(1,11):
    print(end="\t")
    for y in range(1,11):
        print("*",end="")
    print()
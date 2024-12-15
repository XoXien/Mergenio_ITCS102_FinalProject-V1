# Diamond (Asterisk)

for x in range (1, 5):
    for y in range (5, x, -1):
        print(" ",end="")
    for z in range (1, x + 1):
        print("*",end="")  
    for a in range (1, x ):
        print("*",end="")
    print()

for b in range (1, 4):
    for c in range (1, b +2):
        print(" ",end="")
    for d in range (4, b, -1):
        print("*",end="")  
    for d in range (3, b, -1):
        print("*",end="")  
    print()
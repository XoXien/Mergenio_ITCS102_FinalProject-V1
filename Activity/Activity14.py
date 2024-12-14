# Left Half Pyramid Generator using While Loop and using Import

import os #Imports the os module for system-specific operations like clearing the console.
repeat = True #Initializes a boolean flag to control the loop.
nt = 0
while repeat == True:
	var = input("Do you wish to add more triangles? (yes/no) ")

	if var.lower() == "no": #To stop the loop
			os.system('cls')
			print("LOOP HAS BEEN STOPPED")
			repeat = False
			break
			
	elif var.lower() == "yes":#To add more triangles
		os.system('cls')
		nt += 1
		for x in range(1,7):
			for z in range(1,nt+1):
				for y in range(1, x+1):
						print("*", end=" ")
				for a in range(7, x, -1):
						print(" ",end=" ")
				print(end=" ")
			print()
		continue
	else:
		print("Invalid Input") 
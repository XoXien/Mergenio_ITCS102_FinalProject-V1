#Grading System Code Challenge
pre = eval(input("Please input your Prelim grade :"))
mid = eval(input("Please input your Midterm grade :"))
semi = eval(input("Please input your Semi-Finals grade:"))
fin = eval(input("Please input your Finals grade:"))
quiz = eval(input("Please input your Quiz grade:"))
project = eval(input("Please input your Project grade:"))

#Final Grade
Fg =(pre * .15)
Fg +=(mid * .15)
Fg +=(semi * .15)
Fg +=(fin * .15)
Fg +=(quiz * .25)
Fg +=(project * .15)

print()

#Decision
print(f"This is your Final grade {round(Fg,2)}")

print()

if Fg >= 75:
	print("Congratulation! You Passed the course")
		
else:
	print("Sorry,You failed")
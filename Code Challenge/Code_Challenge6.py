#Age Categorizer
name =input("Enter your name:") 
age = int(input("enter your age:"))

print() #blank line or space in output

#Ages
if age >=1 and age <=8:
	print(f"Hi,{name} your age is categorized as Toddler")
elif age >=9 and age <=14:
	print(f"Hi,{name} your age is categorized as Pre Teen")
elif age >=15 and age <=18:
	print(f"Hi,{name} your age is categorized as Teenager")
elif age >=19 and age <=27:
	print(f"Hi,{name} your age is categorized as Early Adulthood")
elif age >=28 and age <=44:
	print(f"Hi,{name} your age is categorized as Middle Age")
elif age >=45 and age <=29:
	print(f"Hi,{name} your age is categorized as Past Adulthood")
elif age >=60 and age <=150:
	print(f"Hi,{name} your age is categorized as Senior")

else:
	print("Invalid Age")
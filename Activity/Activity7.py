#Nested Conditional Statement

name = input("Enter your name: ")
isEnrolled = input("Are you enrolled in DLL (yes/no): ")

if isEnrolled.lower() == "yes":
    print(f"Hi {name}, Welcome to DLL scholarship application")
    print()
    
    age = eval(input("Enter your age: "))
    if age >= 18 and age <= 35 :
        print("Your age is qualified with the age requirement")
        print()

        grade = eval(input("Enter your GWA here: "))
        if grade >= 85 and age <= 99:
            print("Your grade is qualified in DLL scholarship application")
            print()

            is4ps = input("Are you a 4ps beneficiary?(yes/no): ")
            if is4ps.lower() == "yes":
                print("All done! Please wait!")
                
            else:
                print("All done! Please wait!")
        else:
            print("Your grade is not qualified in DLL scholarship application")        
    else:
        print("Sorry, Your age is not qualified with the age requirement (18-35) ")
else :
    print("Sorry, You're not qualified to DLL scholarship application ")




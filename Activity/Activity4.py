#Celsius to Farenheit
#F=Fahrenheit C=Celsius
# Conversion
F = eval(input("Enter Temperature in FARENHEIT: "))

#Formula 
C = ((F - 32)*5)/9
round(C,2) # To limit the decimal into two (2) places

#Output
print(f"{F} degrees in Farenheit converted to Celsius is {C}")

#Farenheit to Celsius
C = eval(input("Enter Temperature in CELSIUS: "))

#Formula
F = (C * 9/5) + 32

#Output
#'Round' can be place directly inside the print 
print(f"{C} degrees in Celsius converted to Farenheit is {round(F,2)}")


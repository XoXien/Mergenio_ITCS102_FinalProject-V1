# Mini Grocery Store Simulator

name = input("Enter your name: ")
purchase = input("Did you purchase a grocery today (yes/no): ")

print()
if purchase.lower() == "yes":
    print(f"Hello! {name} welcome to the Counter")

    # Product and payment details
    product = input("What item did you purchase: ")  
    price = eval(input("Item price: "))  
    age = eval(input("Age: "))  

    print()
    # 3.8% discount if the untaxed price is more than 4000
    if price > 4000:
        PDiscount = round(price * 0.038, 2)
        # Apply the discount
        discounted_price = price - PDiscount  
        print(f"Discount of 3.8% applied: {PDiscount}")
    else:
        discounted_price = price
        print(f"Your purchase product worth of {price} is not eligible for discount.")
    
    # Calculate tax on the discounted price
    Tax = round(discounted_price * 0.123, 2)
    print(f"Tax of 12.3% applied: {Tax}")
    
    # Total price after discount and tax
    total_price = round(discounted_price + Tax, 2)

    # Senior discount if age is more than 60 but not higher than 150
    if 60 < age <= 150:
        SDiscount = round(total_price * 0.123, 2)
        # Apply the senior discount  
        total_price -= SDiscount          
        print(f"Senior discount of 12.3% applied: {SDiscount}")
    else:
        print(f"Your age of {age} is not eligible for senior discount.")
    
    print(f"Total price after tax and discounts: {round(total_price, 2)}")
    
    print()
    # Check if the payment is enough and calculate change
    payment = eval(input("Payment amount: "))
    if payment >= total_price:
        change = round(payment - total_price, 2)
        print(f"Hi, customer {name} your total purchase after Tax and Discount is {round(total_price, 2)} and your payment is {payment}")
        print(f"Thank you for your payment. Your change is: {round(change, 2)}")
    else:
        balance = round(total_price - payment, 2)
        print(f"Insufficient payment. You still owe: {round(balance, 2)}")
else:
    print("Thank you for using the system.")

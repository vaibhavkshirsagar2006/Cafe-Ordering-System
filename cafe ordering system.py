from colorama import Fore, Style
from datetime import datetime

customer = [
    input("Enter your name: "),
    input("Enter your mobile number: "),
    input("Enter your email (optional): ")
]


prices = {
    "coffee": 20.00,
    "tea": 10.00,
    "pastry": 30.00,
    "pizza": 100.00,
    "sandwich": 50.00,
    "cold_drink": 40.00,
    "burger": 60.00
}


quantities = {
    "coffee": 0,
    "tea": 0,
    "pastry": 0,
    "pizza": 0,
    "sandwich": 0,
    "cold_drink": 0,
    "burger": 0
}

print("\nWelcome to Cafe Corner!")
print("Menu:")
print("1. Coffee - ₹20.00")
print("2. Tea - ₹10.00")
print("3. Pastry - ₹30.00")
print("4. Pizza - ₹100.00 (Large), ₹70.00 (Medium)")
print("5. Sandwich - ₹50.00")
print("6. Cold Drink - ₹40.00")
print("7. Burger - ₹60.00")


while True:
    item = int(input("\nEnter item number to order: "))
    
    if item == 1:
        qty = int(input("How many coffees? "))
        quantities["coffee"] += qty
    elif item == 2:
        qty = int(input("How many teas? "))
        quantities["tea"] += qty
    elif item == 3:
        qty = int(input("How many pastries? "))
        quantities["pastry"] += qty
    elif item == 4:
        size = input("Choose size (Medium(m)/Large(l)): ").lower()
        prices["pizza"] = 70 if size == 'm' else 100
        qty = int(input("How many pizzas? "))
        quantities["pizza"] += qty
    elif item == 5:
        qty = int(input("How many sandwiches? "))
        quantities["sandwich"] += qty
    elif item == 6:
        qty = int(input("How many cold drinks? "))
        quantities["cold_drink"] += qty
    elif item == 7:
        qty = int(input("How many burgers? "))
        quantities["burger"] += qty
    else:
        print("Invalid selection. Try again.")
        continue

    another = input("Do you want to order another item? (1 for Yes / 0 for No): ")
    if another != '1':
        break


total = sum(quantities[item] * prices[item] for item in quantities)
discount = 0
if total > 1000:
    discount = total * 0.05
    total -= discount
    print(f"\n{Fore.GREEN}{Style.BRIGHT}🎉 5% discount applied! 🎉{Style.RESET_ALL}")
    print(f"{Fore.RED}You saved ₹{discount:.2f}{Style.RESET_ALL}")


print("\n----- Order Summary -----")
for item in quantities:
    if quantities[item] > 0:
        print(f"{item.replace('_', ' ').title()}: {quantities[item]} x ₹{prices[item]} = ₹{quantities[item] * prices[item]}")

print(f"\n{Fore.CYAN}{Style.BRIGHT}💰 Total Bill: ₹{total:.2f} 💰{Style.RESET_ALL}")

def payment(total):
    print("\nPayment Options:")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")
    method_input = input("Choose payment method (1/2/3): ")
    methods = {'1': 'Cash', '2': 'UPI', '3': 'Card'}
    method = methods.get(method_input, 'Cash')
    print(f"\nProcessing {method} payment of ₹{total:.2f}...")
    print(f"{Fore.CYAN}Payment Successful!{Style.RESET_ALL}")
    return method


def receipt(customer, quantities, total, discount, payment_method):
    print("\n----- Cafe Corner Receipt -----")
    print(f"Customer Name: {customer[0]}")
    print(f"Mobile: {customer[1]}")
    if customer[2]:
        print(f"Email: {customer[2]}")
    print("\nItems Ordered:")
    for item in quantities:
        if quantities[item] > 0:
            print(f"{item.title()} x {quantities[item]} = ₹{quantities[item] * prices[item]}")
    if discount > 0:
        print(f"Discount: ₹{discount:.2f}")
    print(f"Total: ₹{total:.2f}")
    print(f"Payment Method: {payment_method}")
    print("Date & Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Thank you for visiting Cafe Corner!")
    print("-------------------------------")


method = payment(total)
receipt(customer, quantities, total, discount, method)


rating = int(input("\nRate your experience from 1 to 5: "))
if rating == 5:
    print("🌟 Thanks for the excellent rating!")
elif rating == 4:
    print("😊 Glad you had a good experience!")
elif rating == 3:
    print("🙂 Thanks, we’ll keep improving!")
elif rating == 2:
    print("😐 Sorry to hear that, we’ll do better.")
elif rating == 1:
    print("😔 We apologize, and we’ll work hard to improve.")
else:
    print("Invalid rating. Please use 1 to 5.")

print("\n🎉 Visit again soon! 🎉")
#define the menu
menu = {
    'pizza' : 140,
    'Biriyani' : 220,
    'Momo' : 45,
    'Chowmin' : 55,
    'pasta' : 120,
}

#Greet
print("----******Welcome to Bhadwa khayenga LAUWDA Restro & Cafe******----")
print("pizza: 140\nBiriyani: 220\nMomo: 45\nChowmin: 55\nPasta: 120")

order_total = 0
item_1 = input("Please give your order Sir!!")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your {item_1} has been ordered")
else:
    print("Order something else that we could serve!!")
another_total = input("Anything else sir?(yes/no)")
if another_total == "Yes":
    item_2 = input("Give another order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your {item_2} Has been booked!!")
    else:
        print("Enter a valid order!")

print(f"The total ammount of items to pay is {order_total}")
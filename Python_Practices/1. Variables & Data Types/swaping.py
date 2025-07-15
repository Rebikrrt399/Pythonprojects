#Write a Python program to swap two variables.
a = input("Enter the First Number:")
b = input("Enter the Second Number:")
print(f"Before swaping with a third variable a = {a} and b = {b}")
c = a 
a = b 
b = c
print(f"After swaping with a third variable a = {a} and b = {b}")
'''
'''
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
print(f"Before swaping without a third variable a = {a} and b = {b}")
a = a+b #a = 12 + 10 = 32 
b = a-b #b = 32 - 10 = 12
a = a-b #a = 32 - 12 = 10
print(f"Before swaping without a third variable a = {a} and b = {b}")

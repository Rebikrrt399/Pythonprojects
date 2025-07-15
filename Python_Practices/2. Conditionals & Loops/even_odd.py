#Write a program to check if a number is even or odd.
while True:
    num = int(input("Enter a number or type quit:"))
    
    if num <= 0:
        print("Abbey thik thak number de bhai sab jaga bakchodi nahi chalti")
        break
    else:
        check = num % 2
        if check == 0:
            print("Given number is EVEN!")
        else:
            print("Given number is ODD!!")
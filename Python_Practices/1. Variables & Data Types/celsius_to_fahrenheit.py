#Convert Celsius to Fahrenheit and vice versa.
while True:
    choice = input("Enter f for converstion celsius to fahrenheit and enter c for fehrenheit to celsius, or quit type q:")

    if choice == "f":
        celsius = float(input("Enter the temperature:"))
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0
        print(f"The conversion cel to fahrenheit is:{fahrenheit}")
    elif choice == "c": 
        fahrenheit = float(input("Enter the temperature:"))
        celsius = (fahrenheit - 32.0) * 5.0 / 9.0
        print(f"The conversion fahrenheit to cel is:{celsius}")
    elif choice == "q":
        print("Exiting the converter. bhagg!!")
        break
    else:
        print("chal be thik se laga choice!!")
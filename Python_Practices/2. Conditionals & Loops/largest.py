# Find the largest among three numbers.
def get_numbers():
    while True:
        user_input = input("Enter numbers separated by space or comma: ")
        parts = user_input.replace(',',' ').split()
        try:
            numbers = [int(x) for x in parts]
            if len(numbers) < 2:
                print("Please enter at least two numbers!")
                continue
            return numbers
        except ValueError:
            print("Invalid input. please enter only numbers")
            

numbers = get_numbers()
largest = max(numbers)
print(f"{largest} is the largest among {', '.join(map(str, numbers))}")
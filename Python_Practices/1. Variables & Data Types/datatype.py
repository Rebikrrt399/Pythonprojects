#Check the data type of different variables.
while True:
    user_input = input("Enter any value (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting program. Bye!")
        break

    try:
        # Try to evaluate the input (e.g., 123 → int, [1,2] → list)
        evaluated_input = eval(user_input)
    except:
        # If eval fails (e.g., plain text), treat as string
        evaluated_input = user_input

    print(f"Value: {evaluated_input:<20} | Type: {type(evaluated_input)}")

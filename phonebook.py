phone_book = {
    "Asutosh": 9987957953,
    "vera": 785643209,
    "gautam": 7877679280,
    "goteya": 6432109567,
}

while True:
    choice = input("Enter your choice create, Read, Update or Delete otherwise Exit:")
    if (choice == "create"):
        key = input("\nEnter the name of that person:")
        value = input("Enter his or her phnone number:")
        phone_book[key] = value
    elif (choice == "read"):
        choice2 = input("\nwhat you want to read, phone number or Name:")
        if choice2 == "phone number":
            value_to_find = int(input("Enter the phone number which you are searching:"))
            find_name = [key for key, value in phone_book.items() if value == value_to_find]
            print(f"Yeah {value_to_find} is in our phone book\n His/Her Name is{find_name}!!!")
        elif choice2 == "name":
           search2 = input("Enter the name which you are searching:")
           phone_number = phone_book[search2]
           print(f"Yeah {search2} is in our phone book\n His/Her phone number is{phone_number}!!!")
    elif(choice == "update"):
       choice3 = input("\nwhat you want to update, phone number or Name:")
       if(choice2 == "phone number"):
        value2 = int(input("Enter his or her updated phnone number:"))
       elif(choice2 == "name"):
        key2 = input("Enter the name of that person which you want to update:")
    elif(choice == "delete"):
       delete_item = input("\nEnter the name of that contact which you want to delete:")
       del phone_book[delete_item]
    elif choice.lower() == "exit":
        break
print(f"{phone_book}")
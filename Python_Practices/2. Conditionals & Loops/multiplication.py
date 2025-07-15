# Print the multiplication table of a number.
num = int(input("Enter the number whose table you want to print:"))
for i in range(1, 10 + 1):
    mul = num * i
    print(f"{num} × {i} = {mul}")
    
# save the table in a txt file
# num = int(input("Enter the number whose table you want to print:"))
# fileName = f"Table of {num}"

# with open(fileName, "w") as file:
#     file.write(f"Multiplication Table for {num}\n")
#     file.write("-" * 30 + "\n")
#     for i in range(1, 10 + 1):
#         res = num * 1
#         line = f"{num} × {i} = {res}\n"
#         file.write(line)
        
# print(f"\n Table of {num} saved sucessfully to '{fileName}!")
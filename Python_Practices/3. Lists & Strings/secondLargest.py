# Find the second largest number
# user_input = input("enter numbers:")
# my_list = list(map(int, user_input.split()))
# unique_list = list(set(my_list))
# if len(unique_list)<2:
#     print("thik se number de 2 se jayada number lagega")
# else:
#     unique_list.sort(reverse=True)
#     print(f"Seconf largest number is:{unique_list[1]}")

#Without sorting
user_input = input("enter numbers:")
my_list = list(map(int, user_input.split()))

first = second = float('-inf')
for num in my_list:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
        
if second == float('-inf'):
    print("No second largest number found!")
else:
    print("Second largest number is: ", second)
#Sum of all numbers from 1 to N

n = int(input(("Enter a number N:")))
sum = 0
for i in range(1, n + 1 ):
    sum += i
print(f"The sum of all number from 1 to {n}: {sum}")

#advance
# while True:
#     choice = input("Type E for even number sum, O for odd number sum and Mx for multiple of X(or type 'exit' to quit): ")
#     if choice.lower() == 'exit':
#         print("Exiting program. Bye!")
#         break
#     n = int(input(("Enter a number N:")))
#     if choice == "E":
#         sum_even = 0
#         for i in range(1, n + 1):
#             if i % 2 == 0:
#                 sum_even += i
#         print(f"The sum of all number from 1 to {n}: {sum_even}")
#     elif choice == "O":
#         sum_odd = 0
#         for j in range(1, n + 1):
#             if j % 2 != 0:
#                 sum_odd += j
#         print(f"The sum of all number from 1 to {n}: {sum_odd}")
#     elif choice == "Mx":
#         x = int(input("Enter a number only which multiplying sum you want: "))
#         mul_sum = 0
#         for k in range(1, n + 1):
#             if k % x == 0:
#                 mul_sum += k
#         print(f"The sum multiple of {x}: {mul_sum}")

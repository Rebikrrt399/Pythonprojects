#Reverse a string without using [::-1].

s = input("Enter a String:")
empty_string = ""
for i in range(len(s) - 1, -1, -1):
    empty_string += s[i]
print("Revered string: ", empty_string)

#(a) Stack implementation
# s = input("Enter a string: ")

# # Step 1: Create an empty stack
# stack = []

# # Step 2: Push all characters into the stack
# for char in s:
#     stack.append(char)

# # Step 3: Pop characters to reverse the string
# reversed_str = ""
# while stack:
#     reversed_str += stack.pop()  # LIFO

# print("Reversed string:", reversed_str)
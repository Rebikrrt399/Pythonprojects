#Check if a string is a palindrome.

s = input("Enter a String:")
s_clean = s.replace(",", " ").lower()
empty_string = ""

for i in range(len(s_clean) - 1, -1, -1):
    empty_string += s_clean[i]
if empty_string == s_clean:
    print("It is an palindrome")
else:
    print("It is not a palindrome")
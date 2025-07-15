#Remove duplicates from a list.
#Approach 1:
# mahine_ka_ration = ["dal", "chawal", "Namak", "Toothpaste", "dal", "bhujiya", "chini", "bhujiya"]
# conSet = set(mahine_ka_ration)#Converting the list to a set
# print(sorted(conSet))

#Approach 2: #give the list in a ordered manner
mahine_ka_ration = ["dal", "chawal", "Namak", "Toothpaste", "dal", "bhujiya", "chini", "bhujiya"]
unique_list = []
for i in mahine_ka_ration:
    if i not in unique_list:
        unique_list.append(i)
        
print("MAA: Kya karta hai 1 cheez 2 2 bar likh diya!!.\nThik se likhke de.")
print("| writing    " * 5 + "     \t")
print(f"Thik se likhne ke bad: {unique_list}")
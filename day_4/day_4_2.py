
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

lengt_of_list = len(names)

rand_int = random.randint(0, lengt_of_list -1)
payee = names[rand_int]
print(f"{payee} will buy the meal for today")





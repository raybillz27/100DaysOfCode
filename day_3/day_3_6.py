# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


combine_string = name1 + name2
lower_case = combine_string.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = int(t + r + u + e)


l = lower_case.count("L")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = int(l + o + v + e)

total = str(true) + str(love)
love_score = int(total)


if love_score < 10 or love_score > 90:
    print(f"your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}")

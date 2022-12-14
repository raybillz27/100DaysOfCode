#calculate time left for you if you were to die at 90
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conv = int(age)
sub = 90
add = sub - conv
day =( add * 365)
week = (add * 52)
month = (add * 12)

print(f"you have {day} days, {week} and {month} left.")

#
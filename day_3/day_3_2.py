# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
body_weight = round((weight) / (height) ** 2)

if body_weight < 18:
   print(f"your BMI is {body_weight}, you are underweight.")
elif body_weight < 25:
     print(f"your BMI is {body_weight}, you have a normal weight.")
elif body_weight < 30:
    print(f"your BMI is {body_weight}, you are slightly  overweight.")
elif body_weight < 35:
    print(f"your BMI is {body_weight}, you have are obese.")  
else:
    print(f"your BMI is {body_weight}, you are clinically obese.")

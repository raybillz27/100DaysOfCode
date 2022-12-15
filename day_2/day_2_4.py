#If the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 
print("welcome to tip calculator")
total_bill = float(input("what is the total  bill: $"))
percentage_tip = int(input("what percentage tip would you like to give: "))
bill_split = int(input("how many people to split the bill: "))

step_1 = total_bill * percentage_tip // 100
step_2 = int(total_bill) + int(step_1)
step_3 = (step_2) / int(bill_split)
step_4 = round(step_3, 2)
finale = "{:.2f}".format(step_3) 
print(f"each person should pay: ${finale}")



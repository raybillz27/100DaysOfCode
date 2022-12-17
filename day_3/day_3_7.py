print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇
choice_1 = input('you are at a crossroad, where do you want to go "right" or "left"\n.').lower()

if choice_1 == "left":
  
  choice_2 = input('you reached a lake unarmed type "swim" to swim across or type "wait" to wiat for a boat\n').lower()
  
  if choice_2 == "wait":
     
     choice_3 = input('you arrived at a door "red","yellow","blue"\n choose a door\n').lower()
     
     if choice_3 == "red":
       
       print(" you were burnt by fire.\n game over.")
     
     elif choice_3 == "blue":
       
       print("you were attacked by a beast.\n game over.")
     
     elif choice_3 == "yellow":
         
         print("you won") 
     
     
  
  else:
   
   print("you were attacked by a shark.\n game over")

else: 
   
   print("you fell into a hole\n game over.")




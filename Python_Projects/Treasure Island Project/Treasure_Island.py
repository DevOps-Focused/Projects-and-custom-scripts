print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You are at the coss road where do you want to go?")
direction = input("Type left or right?\n")
direction = direction.lower()

if direction == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.\n")
    lake = input('''Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    lake = lake.lower()
    if lake == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.\n")
        doors = input("One red, one yellow and one blue. Which colour do you choose?\n")
        doors = doors.lower()
        if doors == 'red':
            print("Lion Caught you. Game Over. You Loose")
        elif doors == 'yellow':
            print("You found the treasure! You Win!")
        elif doors == 'blue':
            print("Someone Murdered you. Game Over. You Loose")
        else:
            print("Please select the give door among red, yellow and blue.")
    elif lake == "swim":
        print("Shark Fish eat you. Game Over")
    else:
        print("Wrong input. Please select from wait or swim.")
elif direction == 'right':
    print("You Die. Game over")
else:
    print("Wrong input. Please select from left or right.")

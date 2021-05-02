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
/______/______/______/______/______/______/______/______/______/______/[Rayhan]
*******************************************************************************
''')
print('Welcome to Treasure Island.')
print('You mission is to find the Treasure.')
print('If you won this game, Then you got a treasure ')
choice_1 = input('You\'are at a crossroad, where do you want to go? Type "Left" or "Right": \n').lower()


if choice_1 == 'left':
    choice_2 = input('You\'ve come to lake. There is an Island in the middle of the Lake. Type "wait" to wait for a boat. Type "swim" to swim across: \n').lower()

    if choice_2 == 'wait':
        choice_3 = input('You arrive at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: \n').lower()

        if choice_3 == 'yellow':
            print('Congratulations! \nYou win this game. You got a treasure.')

        elif choice_3 == 'red':
            print("it's room full of fire. Game Over.")

        elif choice_3 == 'blue':
            print("You enter a room of beasts. Game Over.")

        else:
            print('You chose a door that doesn\'t exist. Game Over.')

    else:
        print('You got attacked by an angry trout. Game Over.')

else:
    print('You fell into a Hole. Game Over.')
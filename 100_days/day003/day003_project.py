import sys

def start_game():
        print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |             o`"=._` , "` `; .". ,  "-._"-._; ;              |
________|_____________ ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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

        # Fork on the road
        print("\n---\n")
        user_input = input(f"You come upon a fork on the road with a sign that reads:\n ___________________________________________ \n|                                           |\n|  <-- River Crossing\tMagic Forest -->  |\n|___________________________________________|\n >> Should you go LEFT or RIGHT?: ")
        if user_input.lower() != "left":
                print(f"\nAs you start your journey the road crumbles under your feet causing you to fall into a newly formed hole. You spend many days in the hole and eventually die of thirst.")
                you_die()


        # River crossing
        print("\n---\n")
        user_input = input(f"You walk down the path after several hours you come across a river. \n >> Should you SWIM across or WAIT?: ")
        if user_input.lower() != "wait":
                print(f"\nYou tie down all the wares on the outside of your backpack and start swimming across the river. As you cross the river a small swarm of fish start bitting you, you try to shake them off and swim back to shore but before you can reach the shore you loose control of your arms and drown.")
                you_die()


        # River doors
        print("\n---\n")
        user_input = input(f"After several days the waters of the river lower and three doors become visible. One is RED, another BLUE, and the last one YELLOW.\n >> Which door do you go through?: ")
        if user_input.lower() == "red":
              print(f"As you open the door a great breath of fire comes through burning you to a crip.")
              you_die()
        elif user_input.lower() == "blue":
              print(f"You open the door and walk through. You wonder around for several hours but get lost and are eaten by beasts.")
              you_die()
        elif user_input.lower() == "yellow":
              print(f"You open the yellow door and step through. As you step through you see the sun shinning and a great green field. You spend the remaining of you days there.\nYOU WIN!!!\n")
              sys.exit()
        else:
              print(f"You are unable to pick a door and die from indecision.")
              you_die()


# You died
def you_die():
    print("\n---\n")
    print(f"\nYOU ARE DEAD... GAME OVER!!!\n")
    sys.exit()


# Redirect application entry point
if __name__ == "__main__":
    start_game()
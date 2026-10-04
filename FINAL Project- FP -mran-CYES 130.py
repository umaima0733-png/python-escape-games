# Escape the Forest Game
# Find the key and escape the forest!
# Avoid the monsters!
# Good luck!

# Player stats
Player = {
    "health": 5,
    "inventory": ["Health Potion"],
    "has_key": False
}

# Show player status
def show_status():
    print(f"Health: {Player['health']}")
    print(f"Inventory: {Player['inventory']}")
    print(f"Has Key: {Player['has_key']}")

# Monster riddle encounter
def monster_riddle():
    print("\nA monster blocks your path and asks you a riddle.")
    print("I am shiny and can help you leave this forest. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "key":
        print("Correct! The monster lets you pass.\n")
        return True
    else:
        print("Wrong answer! The monster attacks you.")
        Player['health'] -= 2
        if Player['health'] <= 0:
            print("You have been killed by the monster. Game Over!")
            return False
        else:
            print(f"Your health is now {Player['health']}\n")
            return True

# Show instructions
def show_instructions():
    print("Welcome to Escape the Forest!")
    print("Commands:")
    print("1. explore - Explore the forest")
    print("2. search - Search for items")
    print("3. use potion - Use a health potion")
    print("4. escape - Try to escape the forest")
    print("5. status - Show your current status")
    print("6. Avoid monsters!")

# Show instructions at the start
show_instructions()

# Game loop
while True:
    command = input("\nEnter command: ").lower()

    if command == "explore":
        print("You explore the forest.")
        print("You encounter a monster!")
        if not monster_riddle():
            break  # Player died

    elif command == "search":
        print("You search the area.")
        direction = input("Where do you want to go next, left or right? ").lower()
        if direction == "left":
            print("You found a key!")
            Player['has_key'] = True
        elif direction == "right":
            print("You fell into a trap and lost 2 health points.")
            Player['health'] -= 2
            if Player['health'] <= 0:
                print("You have been killed by the monsters. Game Over!")
                break
            else:
                print(f"Your health is now {Player['health']}")
        else:
            print("Invalid direction. Try 'left' or 'right'.")

    elif command == "use potion":
        if "Health Potion" in Player['inventory']:
            Player['health'] += 3
            Player['inventory'].remove("Health Potion")
            print("You used a health potion. Health increased by 3.")
        else:
            print("You don't have any health potions.")

    elif command == "status":
        show_status()

    elif command == "escape":
        if Player['has_key']:
            print("You used the key to escape the forest. You win!")
            break
        else:
            print("You need a key to escape the forest.")

    else:
        print("Invalid command. Try again.")

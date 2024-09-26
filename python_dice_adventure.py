import random
 
print("Welcome to the Dice Adventure!")
print("You must roll the dice to determine your fate!")
 
while True:
    input("Press Enter to roll the dice...")
    dice_value = random.randint(1, 6)
    print(f"You rolled: {dice_value}")
 
    # Story-based outcomes
    if dice_value == 6:
        print("Amazing! You found a treasure!")
    elif dice_value == 5:
        print("You fought off a wild beast and survived!")
    elif dice_value == 4:
        print("You discover a hidden path in the forest.")
    elif dice_value == 3:
        print("You encounter a river, and must build a raft.")
    elif dice_value == 2:
        print("You slipped and fell into a trap!")
    else:
        print("You rolled a 1... It’s a bad day.")
 
    if input("Roll again? (y/n): ").lower() != 'y':
        break
 
 
 
 
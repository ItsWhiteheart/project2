import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def play_game():
    while True:
        dice1, dice2 = roll_dice()
        roll_sum = dice1 + dice2
        print(f"The dice roll result is {roll_sum}")

        if roll_sum == 7 or roll_sum == 11:
            print("You win!")
            break
        elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
            print("Craps! You lose.")
            break
        else:
            goal_num = roll_sum
            print(f"{goal_num} is your goal number. Roll again.")
            while True:
                dice1, dice2 = roll_dice()
                roll_sum = dice1 + dice2
                print(f"The dice roll result is {roll_sum}")
                if roll_sum == goal_num:
                    print("You win!")
                    return
                elif roll_sum == 7:
                    print("You lose.")
                    return


play_game()



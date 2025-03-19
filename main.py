import random

print("***** Welcome to Snake Water Gun Game ***** ")

n = input("Press 2 to Play | Press 3 to Exit: ")

while n == "2":  # Continue the game if user enters "2"
    computer = random.choice([-1, 0, 1])
    your = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

    yourdict = {"s": -1, "w": 0, "g": 1}
    reverse = {-1: "snake", 0: "water", 1: "gun"}

    if your in yourdict:
        you = yourdict[your]
        print(f"Computer's choice: {reverse[computer]}, Your choice: {reverse[you]}")

        if computer == you:
            print("It's a Draw!")
        else:
            if computer == -1 and you == 1:
                print("You win")
            elif computer == -1 and you == 0:
                print("You lose")
            elif computer == 1 and you == 0:
                print("You win")
            elif computer == 1 and you == -1:
                print("You lose")    
            elif computer == 0 and you == -1:
                print("You win")
            elif computer == 0 and you == 1:
                print("You lose")
            else:
                print("**** Not a valid input ****")

    else:
        print("Invalid input! Please enter 's', 'w', or 'g'.")

    n = input("\nPress 2 to Play Again | Press 3 to Exit: ")  # Ask user again

print("Thanks for playing! Goodbye.")

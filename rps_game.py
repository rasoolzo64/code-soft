import random

print("Welcome to Rock, Paper, Scissors game")

user_name = input("Enter your name: ")

print("""
Rules:
1. Rock vs Paper --> Paper wins
2. Rock vs Scissors --> Rock wins
3. Paper vs Scissors --> Scissors wins
""")

user_score = 0
comp_score = 0
ties = 0

while True:
    print("Select your option from the following:")
    print("""
    1. Rock
    2. Paper
    3. Scissors
    """)
    choice = int(input(f"Enter your choice, {user_name}: "))

    while choice < 1 or choice > 3:
        choice = int(input(f"Choose a valid input, {user_name}: "))

    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissors"

    print(f"Your choice is {user_choice}\n")

    print("----Now it's the computer's turn----")

    comp_choice = random.choice(["rock", "paper", "scissors"])

    print(f"Computer's choice is {comp_choice}\n")

    if (user_choice == "rock" and comp_choice == "paper") or (user_choice == "paper" and comp_choice == "rock"):
        result = "paper"
    elif (user_choice == "paper" and comp_choice == "scissors") or (user_choice == "scissors" and comp_choice == "paper"):
        result = "scissors"
    else:
        result = "rock"

    if user_choice == comp_choice:
        print("It's a tie!")
        ties += 1
    elif result == user_choice:
        print(f"{user_name} wins the game!")
        user_score += 1
    else:
        print("Computer wins the game!")
        comp_score += 1

    print(f"Computer score = {comp_score}")
    print(f"{user_name} score = {user_score}")
    print(f"Ties = {ties}")

    play_again = input(f"Do you want to play again, {user_name}? (Enter 'n' for no or 'y' for yes): ").lower()
    if play_again == 'n':
        break

print(f"Game is completed, {user_name}")

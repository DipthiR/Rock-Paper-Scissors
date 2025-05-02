import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def get_choice_name(choice_number):
    return {1: "Rock", 2: "Paper", 3: "Scissors"}.get(choice_number, "Invalid choice")

def play_game():
    while True:
        print("\nChoose:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Exit")

        try:
            user_choice = int(input("Enter your choice (0/1/2/3): "))
            if user_choice == 0:
                print("Thanks for playing! Goodbye.")
                break
            elif user_choice not in [1, 2, 3]:
                print("Invalid input. Please choose 0, 1, 2, or 3.")
                continue

            computer_choice = random.randint(1, 3)

            print(f"\nYou chose: {get_choice_name(user_choice)}")
            print(f"Computer chose: {get_choice_name(computer_choice)}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

        except ValueError:
            print("Please enter a valid number (0, 1, 2, or 3).")

if __name__ == "__main__":
    play_game()

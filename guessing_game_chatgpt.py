import random

def show_score(attempts_list):
    """
    Display the current high score if available, or prompt the user to start playing.
    """
    if not attempts_list:
        print("There's no high score yet. Start playing to set a high score.")
    else:
        print(f"The current high score is {min(attempts_list)}")

def play_guessing_game():
    """
    Main function to execute the guessing game.
    """
    # List to store the number of attempts for each game
    attempts_list = []

    # Welcome and get user's name
    user_name = input("What's your name: ")

    while True:
        wanna_play = input(f"Welcome, {user_name}! Would you like to play the guessing game? "
                           "Enter (Yes / No): ").lower()

        if wanna_play == 'no':
            print("That's cool. Have a nice day!")
            break
        elif wanna_play == 'yes':
            play_single_game(attempts_list)
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def play_single_game(attempts_list):
    """
    Play a single round of the guessing game.
    """
    rand_num = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))

            if not (1 <= guess <= 10):
                raise ValueError("Please give a number between the given range!")

            attempts += 1

            if guess == rand_num:
                handle_correct_guess(attempts, attempts_list)
                break
            elif guess > rand_num:
                print("It's lower!")
            else:
                print("It's higher!")

        except ValueError as er:
            print(er)

def handle_correct_guess(attempts, attempts_list):
    """
    Handle the case when the user makes the correct guess.
    """
    print("Nice, you got it!")
    print(f"It took you {attempts} attempts to get it.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Yes/No): ").lower()

    attempts_list.append(attempts)

    if play_again == 'no':
        print("That's cool. Have a nice day!")
    elif play_again == 'yes':
        show_score(attempts_list)
    else:
        print("Invalid input. Exiting the game.")

if __name__ == "__main__":
    play_guessing_game()

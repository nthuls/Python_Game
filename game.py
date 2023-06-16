import random

def guess_number():
    while True:
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        attempts = 0

        while True:
            user_guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")

            if user_guess.lower() == "q":
                print("Thanks for playing. Goodbye!")
                return

            try:
                user_guess = int(user_guess)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
                continue

            attempts += 1

            if user_guess < random_number:
                print("Too low. Try again!")
            elif user_guess > random_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {random_number} correctly.")
                print(f"It took you {attempts} attempts to win the game.")
                break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing. Goodbye!")
            return

guess_number()

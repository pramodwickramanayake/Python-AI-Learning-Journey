import random

def start_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Get user input
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Logic to check the guess
            if guess < secret_number:
                print("Too Low! Try a higher number.")
            elif guess > secret_number:
                print("Too High! Try a lower number.")
            else:
                print(f"Excellent! you guessed the correct number in {attempts} attempts.")
                break # Stop the loop

        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# Execute the game
if __name__ == "__main__":
    start_game()
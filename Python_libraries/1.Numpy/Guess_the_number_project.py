import numpy as np

print("===== Guess The Number Game =====")
print("Guess a number between 0 and 100")
print("Type 'exit' to quit the game")

number = np.random.randint(0, 101)
attempts = 0

while True:
    guess = input("\nEnter your guess: ")

    if guess.lower() == "exit":
        print("\nGame Over!")
        break

    guess = int(guess)
    attempts += 1

    if guess > number:
        print("Lower!")

    elif guess < number:
        print("Higher!")

    else:
        print("\nCongratulations! You guessed it.")
        print("You took", attempts, "attempt(s).")

        print("\n===== Score Board =====")
        print("Correct Number :", number)
        print("Attempts       :", attempts)

        break
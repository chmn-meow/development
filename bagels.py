import random

NUM_DIGITS = 3  # Try between 1 or 10
MAX_GUESSES = 10  # Try between 1 or 100


def main():
    print(
        """***Translated from Python2***\n\r
    Bagels, a deductive logic game.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the 
    clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        print("Do you want to play again? (yes or no)")
        if not input("> ".lower().startswith("y")):
            break
    print("Thanks for playing!")


def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_number = ""
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # a correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # a correct digit is in the incorrect place
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()

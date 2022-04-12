# Guessing Game
# User keeps on guessing the secret word until they get their response right

secret_word = "giraffe"
# Variable to store users guest
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    # Check user guess limit
    if guess_count < guess_limit:
        if(guess != ""):
            print("Your guess is not correct. Try again")
        # Get user input
        guess = input("Enter the secret word mate: ")
        # Update guess count
        guess_count += 1
    else:
        out_of_guesses = True

# Print result
if out_of_guesses:
    print("Sorry you lost. Out of guesses.")
else:
    print("Alright, you got it correct. The secret word is "+secret_word+"!!")

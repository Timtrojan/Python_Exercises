import random

number_to_be_guessed = 78
guess_times = 0
while guess_times < 3:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number_to_be_guessed:
        print("You are correct")
        break
    else:
        if guess > number_to_be_guessed:
            print("Your guess is higher than the right answer")
        if guess < number_to_be_guessed:
            print("your guess is lower than the right answer")

        guess_times += 1
if guess_times == 3:
    print("try again ")

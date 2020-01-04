import random

name = input("Enter is your name:")
print(
    "\nHello " + name + "!!! \nI am guesswork \nI am going to choose a number between 1-100. \nYour job is to guess "
                        "that number. \nYou have 6 "
                        "chances to guess that number.")
num_guesses = 0
number = random.randint(0, 100)

while num_guesses < 6:
    num_guesses = num_guesses + 1
    guess = int(input("\nEnter your guess: "))
    if guess < number:
        print("Go up a value!!!")
    if guess > number:
        print("Go down the value!!!")
    if guess == number:
        break

if guess == number:
    num_guesses = str(num_guesses)
    print("Congratulations!!! " + name + " You guessed the right number after " + num_guesses + " number of guesse(s)")
if guess != number:
    number = str(number)
    print(name + " you failed!!! \nnumber was " + number + "\nBetter luck next time")

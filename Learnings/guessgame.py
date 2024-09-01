import random

n = random.randrange(1, 10)
guess = int(input("Enter any number between 1 and 10: "))

while n != guess:
    if guess < n:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Enter the number again: "))

print("You guessed it right!!")

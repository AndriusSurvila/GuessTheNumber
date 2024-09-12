import random

nums = [i for i in range(1, 101)]
guess = input("Guess a number between 1 and 100: ")
num = random.choice(nums)

while int(guess) != num:
    if int(guess) > num:
        guess = input("Too high. Guess again: ")
    else:
        guess = input("Too low. Guess again: ")

print("Correct!")
import random

n = random.randrange(1, 10)
guess = int(input("Guess a number between 1 and 10:"))
while guess != n:
	if guess < n:
		print("Guess a higher one. Try again!")
		guess = int(input("Guess a number between 1 and 10:"))
	else:
		print("Guess a lower one. Try again!")
		guess = int(input("Guess a number between 1 and 10:"))
print("Guessed the correct number!")

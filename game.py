"""
Guess the number in Python
It's a terminal game
The number to guess is between 1 and 100 and the player has 10 tries to guess it
Beginner's Python program
"""

import random # for randint()

print("\nGuess the number game\n")

# make an infinite loop for the play again system
while True:

	# define the number to guess with randint()
	number = random.randint(1, 100)
	# initialize the counter
	counter = 0

	print("I'm thinking of a number between 1 and 100, you have 10 tries to guess it")

	while counter < 10:
		guess = int(input("Try to guess\n"))
		counter+=1

		if guess == number:
			break
		elif guess < number:
			print("Too low!")
		else:
			print("Too high!")


	if guess == number:
		# the player won
		print("\nCongratulations! You won in " + str(counter) + " tries.")
	else:
		# the player lost
		print("\nYou lost, I was thinking of " + str(number))

	# ask to play again
	if input("\nDo you wanna play again ? (y/n)\n") != "y":
		break

print("\nThanks for playing!\n")
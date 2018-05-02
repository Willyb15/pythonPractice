import random

#boolean, which will be a flag/switch
keep_playing = True

# Get the loop going as long as the bool is true
while keep_playing == True:
	#Get a random number between 1-10
	correct_number = random.randint(1,10)
	print correct_number

	keep_guessing = True
	total_tries = 5
	used_tries = 0

	while keep_guessing == True:
		#Get a guess from the user
		guess = int(raw_input('Guess a number between 1-10\n'))
		used_tries += 1
		if(guess == correct_number):
			print "You Win"
			keep_guessing = False
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
		elif(total_tries == used_tries):
			print 'Sorry You are out of guesses. The number was %d' % correct_number
			keep_guessing = False
		else:
			if(guess < correct_number):
				print "Too Low"
			else:
				print "Too High"
	play_again = raw_input('Would you like to play agian? Enter yes or no\n')

	if(play_again == 'yes'):
		keep_playing = True
	else:
		keep_playing = False
		print 'thank you for playing'
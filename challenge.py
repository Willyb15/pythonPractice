
# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
# Python is dnyamic! We don't have a "Declare" step.
# We just make them!.

fullName = "Will Bryant"
age = 31



# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.



# So... there are no arrays. But there are lists!.
# There is no push... but there is append!.
# myArray = []
# myArray.append(fullName)
# myArray.append(age)
# print myArray



 # 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.
# Function = defintion in python.

# def sayHello():
# 	print 'hello'

# sayHello()


# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed 
# in the instructions PDF.

# fullName = "Will Bryant"
# splitName = fullName.split(' ')
# print splitName


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

# def sayName():
# 	entry = raw_input('>>>>>')
# 	# print 'Hello, ' % splitName[0]
# 	print 'Hello, ' + entry

# sayName()

# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.



import datetime
now = datetime.datetime.now()
print now
currentyear = now.year
print currentyear


def myAge(yearyouwereborn):
	print currentyear - yearyouwereborn

myAge(1986)


# 7) Using the basic function given below, add code so that sum_odd_numbers 
# will print to the console the sum of all the odd numbers from 1 to 5000.  
# Don't forget to call the function!
# HINT: Consider using a 'for loop'.

def sumOdd():
	sum = 0
	for i in range (1, 5001):
		if (i % 2 == 1):
			sum += i
	print sum

sumOdd()


def sumOdd2():
	sum = 0
	# range has a 3rd arg. Step is the thrid, so you can run the 
	# loop by 2s (instead of 1s)
	# for i in range(1,5001,2):
	for i in range(4999,0,-2):
		sum += i
	print sum

sumOdd2()

def sumOdd3():
	i = 1
	sum = 0
	while 1:
		sum += i
		i += 2
		if (i >=5000):
			break
	print sum

sumOdd3()






































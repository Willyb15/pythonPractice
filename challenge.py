
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

def sayHello():
	print 'hello'

sayHello()


# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed 
# in the instructions PDF.

fullName = "Will Bryant"
splitName = fullName.split(' ')
print splitName


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

def sayName():
	entry = raw_input('>>>>>')
	# print 'Hello, ' % splitName[0]
	print 'Hello, ' + entry

sayName()































# A function (in Python 'definittion'), is a peive of c
# ode that can be called from somehwere else
# # They are meant to be reusable to keep code clean

# If you have complicated code, you can break it into peices that are
# easier to understand

# Repeating yourself is bad
# copy paste errors
# odd behavior
# to declare a function in python, you use 'def'
# functions always have a ()

# this defines the function
def say_hello():
	print 'hello'

# This calls the function (tells Python to run the code inside say_hello def)
say_hello()

# passing variables into functions, are called arguments on the way in
# parameters once inside

def say_hello_with_name(name):
	print 'Hello, %s' % name

say_hello_with_name('Will')

players = ['Will', 'Brian', 'Ben', 'Matt']
for i in range (0, len(players)):
	say_hello_with_name(players[i])

# say_hello_with_name()
# The above line will FAIL!!

# You can set a default for a parameter
def say_hello_safe(name, in_game="Yes"):
	print "%s, %s is in the game" % (in_game, name)


say_hello_safe('Bob')
say_hello_safe('Will')

say_hello_safe("tony")
say_hello_safe("ryan", "No")

# functions ALWAYS return a value
# return value is a functions chance to send ONE and only ONE thing back to 
# whoever calle it

def return_player_name(name):
	normalized_name = name.upper()
	return normalized_name

print return_player_name('will')


print return_player_name("Im a WiLD anD CrAZy GUy")











































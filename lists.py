player1 = 'Will'
player2 = 'Brian'
player3 = 'Matt'
player4 = 'Ben'

# print player1

# a list is a single variable with a bunch of numbered (indexed parts)
# an index in a list is AWLWASY a number
# A list is made with []

# players = ['Will', 'Brian']

# I know the Thrashers are gone
atlanta_teams = [
	'Falcons',
	'Braves',
	'Hawks',
	'Thrashers'
]

# print atlanta_teams
# # Remove an element from the end with "pop"
# atlanta_teams.pop()
# print atlanta_teams
# print atlanta_teams

# atlanta_teams.pop()
# print atlanta_teams
atlanta_teams.append('ATL United')
# print atlanta_teams

# Loop from 0-5
# for i in range (0,5)


# for i in range(0, len(atlanta_teams)):
# 	if (atlanta_teams[i] == 'Thrashers'):
# 		thrasher_index = i
# 		# break means stop the loop. I dont care about the condition
# 		break

# atlanta_teams.pop(thrasher_index)
# print atlanta_teams


# split turns a sting into a list
teams_as_a_string = 'Falcons, Braves, Hawks, United'
print teams_as_a_string

teams_as_a_list = teams_as_a_string.split(', ')
print teams_as_a_list

# lists also have a sort method
# sort will change the list
# sorted atlanta_teams
# atlanta_teams.sort()
# print atlanta_teams

sorted_atlanta_teams = sorted(atlanta_teams)
print atlanta_teams
print sorted_atlanta_teams

sorted_atlanta_teams.reverse()
print sorted_atlanta_teams



# if you want to copy part of the list, you can use [x:y]
# this will create a copy of the array. it will not chnage the original
# it will start at the xth element, and stop at the yth
# so if we want braves and hawsk 1,2, we start at 1 amd stop at 3



baseball_basketball = atlanta_teams[1:3]
print baseball_basketball

all_but_first = atlanta_teams[1:]
print all_but_first

# to delete an index, you can use the remove method
# alternative to pop, you prove the element istead of the idnex

atlanta_teams.remove("Braves")
print atlanta_teams

# insert we can insert an element whereever we want!!

atlanta_teams.insert(1, "Braves")
print atlanta_teams

atlanta_teams.insert(0,"Tom Bradys Team")
print atlanta_teams


















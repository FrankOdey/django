def people(students):
    print(students)

people('Frank')
# (study) is the argument the function takes.
# (Frank) is the parameter pass in to the function call as the argument (study)

#EXAMPLE 2
people('Mary') # Value parameter pass in as argument.
james = "I'm James"
people(james) # Variable parameter pass in as argument.
people('Rita \n'*4) # Expression pass in as argument.

# EXAMPLE 3
def gameShow(numPlayers):
    print(str(numPlayers) + ' is the maximum require at this level')

gameShow(500)
#Outside the function.
print(str(numPlayers) + ' is not available')
# numPlayers is not accessible outside the function define because it's the function local variable
#  and so should be use only in the function body.

#EXAMPLE 4
def fruit(color):
    print('Every fruit has a color of ' + color)

fruit('yellow')
#Outside the function.
print(yellow + 'is the fruit color')

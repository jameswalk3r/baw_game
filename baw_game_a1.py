#Libraries to import
import random
import dice


# Code to support print_and_wait() across platforms
# Should only be run once, rather than within the function for better performance
try:
    # Win32 (If running on a windows machine, then this will just import getch)
    from msvcrt import getch
except ImportError:
    # If not running on windows, then getch will be defined below. 
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
def print_and_wait(wait_text):
    print(wait_text)
    getch()


#WELCOME TO THE GAME
print_and_wait('Welcome to the game! \nPress any key to continue...') # the \n is a way to start a new line in terminal when writing a terminal message

#Core Ideas
#Player creates character's name
player_name = input('What is your character\'s name?\n')
print('Your character\'s name is ' + player_name)
print_and_wait('Welcome to your adventure ' + player_name + '. Your destiny awaits!')
print (' ')

#Player selects Race and Class. 
print ('''Please type the number for your chosen race. 
If you would like to pick a random race, select 0. \n''')
 
races = { 1 : 'Human', 2 : 'Elven', 3 : 'Half-Blood'}
for each_race in races:
    print(each_race, races[each_race])

player_race = int(input())

print ('You have selected ' + str(player_race))

if player_race == 0:
    player_race = dice.roll(1,3) # What happens if we add more races?
elif player_race > 3: #This is NOT going to work long term. What happens if they type a alpha?
    # What happens if we add more races?
    print('Please make a valid choice.')
    player_race = int(input())

print_and_wait('You have chosen to be ' + races[player_race])

#Class = How fast certain skills level up and slight skill boosts.

#Skill levels 1-50; Race gives boosts to cetain skills.
#Skills: Combat, Stealth, Magic, and Speech
#Genetic Skills level by +10, class by +5, use by +1.
#Level Speed is for Non-Genetic Skills.

#Races: Human(2), Elven(2), Half-Blood(1)
#Human 1: Well-rounded; not best in any skills. Level speed slow.
#Human 2: Low Stealth, high Speech. Level up speed medium.
#Elven 1: Low Combat, high Magic. Level up speed medium/fast.
#Elven 2: Low Combat, high Stealth. Level up speed medium.
#Half-Blood: Low stealth, high magic. Level speed medium.

#Player selects class.
print('What is your character\'s class?\n')
c = int(input('Press 1 for Warrior, 2 for Mage, or 3 for Assassin.\n'))
if c == 1:
    print('Warrior class selected')
elif c == 2:
    print('Mage class selected')
elif c == 3:
    print('Assassin class selected')




#Start of our adventure

print (player_name + '... Welcome to The Crystal Key!\n' + '\n')
print ('''You have found yourself in dank musky dungeon deep under the ancient ruins Kalkavar, \
with no memory of how you got there...  You realize you're at an intersection. \n''')
player_move = int(input ('Which way do you want to go?\n\n 1.) Press Forward\n 2.) Turn Back\n 3.) Explore Other Reigons of the Ruins\n'))
if player_move == 1:
    print ('You have decided to press forward.')
elif player_move == 2:
    print ('You have decided to turn back.')
elif player_move == 3:
    print ('You have decided to explore the ruins further\n')
    explore_choice = input ('Which way do you want to go?\n Left or Right?\n')
    if str.lower(explore_choice) ==  'left':
        print ('something')
    elif str.lower(explore_choice) ==  'right':
        print ('something else')



print_and_wait("\n\n\n\n\nThank you for testing our game!")
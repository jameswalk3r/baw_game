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
print_and_wait('Welcome to The Crystal Key! \nPress any key to continue...\n') # the \n is a way to start a new line in terminal when writing a terminal message

#Core Ideas
#Player creates character's name
player_name = input('What is your character\'s name?\n')
print('Your character\'s name is ' + player_name)
print_and_wait('Welcome to your adventure ' + player_name + '. Your destiny awaits!\n')


#Player selects Race and Class. 
print ('''Please type the number for your chosen race. 
If you would like to pick a random race, select 0. \n''')
 
races = { 1 : 'Human', 2 : 'Elven', 3 : 'Half-Blood'}
for each_race in races:
    print(each_race, races[each_race])

player_race = int(input())

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
print('\nWhat is your character\'s class?\n')
player_class = int(input('Press 1 for Warrior, 2 for Mage, or 3 for Assassin.\n'))
if player_class == 1:
    print('Warrior class selected\n\n')
elif player_class == 2:
    print('Mage class selected\n\n')
elif player_class == 3:
    print('Assassin class selected\n\n')



# player_name = 'TESTNAME'
# player_race = 1
# player_class = 1

#Start of our adventure

print ('''You have found yourself in dank musky dungeon deep under the ancient ruins of Kalkavar, \
with no memory of how you got there...\n  You realize you're at an intersection. \n''')
player_move = int(input ('Which way do you want to go?\n\n 1.) Press Forward\n 2.) Turn Back\n 3.) Explore Other Reigons of the Ruins\n'))
if player_move == 1:
    print ('You have decided to press forward.')
elif player_move == 2:
    print ('You have decided to turn back.')
elif player_move == 3:
    print ('You have decided to explore the ruins further\n')
    explore_choice = input ('Which way do you want to go?\n Left or Right?\n')
    if str.lower(explore_choice) ==  'left':
        player_1_choice = int(input ('There is a steep drop, it\'s safe to go down but you won\'t be able to get back up.\n\n 1.)Drop Down\n 2.)Turn Back\n'))
        if player_1_choice == 1:
            print ('drop placeholder')
        if player_1_choice == 2:
            print ('back placeholder')
    if str.lower(explore_choice) ==  'right':
        player_1_choice = int(input ('You look down and see a tunnel with a chest at the bottom.\n\n 1.)Drop Down\n 2.)Turn Back\n'))
        if player_1L_choice == 1:
            print ('drop placeholder')
        if player_1L_choice == 2:
            print ('back placeholder')


print_and_wait("\n\n\n\n\nThank you for testing our game!")
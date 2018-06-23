#Libraries to import
import random
import dice
import os

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

# Creating a stats object. This will be used to print the player's statistics at the 
# top of each screen. 
stats = ''
def add_stats(new_stat_label, new_stat_value):
    global stats
    stats = stats + '   ' + new_stat_label + ': ' + new_stat_value

# Creates a function that easily clears the screen, depending on the operating system. 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# This funtion makes it easy to print text and allow the user to choose
# when they're ready to continue. 
def print_and_wait(your_text):
    print(your_text)
    print('\n\n\nPress any key to contine...')
    getch()
    clear_screen()

def print_perma_bar():
    clear_screen()
    print(stats + '\n') 

#WELCOME TO THE GAME
clear_screen()
print('Welcome to The Crystal Key! ') # the \n is a way to start a new line in terminal when writing a terminal message
print_and_wait('''
___________.__             _________                         __         .__     ____  __.            
\__    ___/|  |__   ____   \_   ___ \_______ ___.__. _______/  |______  |  |   |    |/ _|____ ___.__.
  |    |   |  |  \_/ __ \  /    \  \/\_  __ <   |  |/  ___/\   __\__  \ |  |   |      <_/ __ <   |  |
  |    |   |   Y  \  ___/  \     \____|  | \/\___  |\___ \  |  |  / __ \|  |__ |    |  \  ___/\___  |
  |____|   |___|  /\___  >  \______  /|__|   / ____/____  > |__| (____  /____/ |____|__ \___  > ____|
                \/     \/          \/        \/         \/            \/               \/   \/\/     
''')


#Core Ideas
#Player creates character's name
player_name = input('What is your character\'s name?\n')
add_stats('Player Name', player_name)
print_perma_bar()

print_and_wait('Welcome to your adventure ' + player_name + '. Your destiny awaits!\n')

#Player selects Race and Class. 
print_perma_bar()
print ('''Please type the number for your chosen race. ''')
 
races = { 1 : 'Human', 2 : 'Elven', 3 : 'Half-Blood'}
for each_race in races:
    print(each_race, races[each_race], '')

player_race = input()

if type(player_race) != int and player_race not in [1,2,3]:
    player_race = dice.roll(1,3) # What happens if we add more races?
    print('''Wrong answer. Your race has been chosen for you.\nThis is why we don\'t have nice things...\n''')

add_stats('Player Race' , races[player_race])
print_and_wait('Congratulations! You have chosen to be ' + races[player_race] + '. Mom would be so proud!')

print_perma_bar()


#Class = How fast certain skills level up and slight skill boosts.

#Skill levels 1-50; Race gives boosts to cetain skills.
#Skills: Combat, Stealth, Magic, and Speech
#Genetic Skills level by +10, class by +5, use by +1.
#Level Speed is for Non-Genetic Skills.

#Races: Human(2), Elven(2), Half-Blood(1)
#Human 1: Well-rounded; not best in any skills. Level speed slow.
#Human 2: Low Stealth, high Speech. Level up speed medium.
#Elven 1: Low Combat, high Magic. Level up speed medium/fast.
    #Elven 2: Low Combat, high StealthZprint_perma_bar()

print_perma_bar()
print('''What is your character\'s class? 
If you would like to pick a random race, select 0.''')
classes = { 1 : 'Warrior', 2 : 'Mage', 3 : 'Assassin'}
for each_class in classes:
    print(each_class, classes[each_class])

player_class = int(input())
add_stats('Player Class' , classes[player_class])

# player_name = 'TESTNAME'
# player_race = 1
# player_class = 1

#Start of our adventure

print_perma_bar()
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
        if player_1_choice == 1:
            print ('drop placeholder')
        if player_1_choice == 2:
            print ('back placeholder')


print_and_wait("\n\n\n\n\nThank you for testing our game!")
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

########################TEST CODE BELOW#######################

# char_age = input('What is your character\'s age?\n')
# print ("You are " + char_age + " years old.")
# n = int(input('give me a number, 1-4\n'))
# if n == 1:
#     print('fart')
# elif n == 2:
#     print('wet fart')
# elif n == 3:
#     print('shard')
# elif n == 4:
#     print('poo')
# else: print('you moron!')

# if 1 == 1:
#     print ('yay')
# if 1 == 1:
#     print ('thats false')
#     if 1 == 2:
#         print ('howdy')
# if 1 == 1:
#     print ('okay')
#     print ('thats whats up')
#     print ('bye')
#     if 1 == 2:
#         print ('howdy')
# print ('bye')

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
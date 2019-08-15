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

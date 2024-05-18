from termcolor import colored

print(colored('Hi There!', color='yellow' , on_color='on_cyan' , attrs=['bold']))
print(colored('Hi There!', color='magenta'))

# inside terminal type help command to gain more information about the module
#1. type py hit enter
#2. type help(termcolor)
#3. type quit() to exit the help mode

# following module will generate an ASCII art
from pyfiglet import figlet_format
print(figlet_format('Hi There!', font='starwars'))
print(colored(figlet_format('Hello!', font='starwars'), color='yellow'))
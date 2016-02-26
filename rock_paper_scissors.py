"""
By JCT Dickinson
Using TextMate 2.0-ß.8.5

Test of tuple vs. list:
$ python3 -m timeit "import random" "tuple = ('1', '2', '3')" "choice = random.choice(tuple)
1000000 loops, best of 3: 1.77 usec per loop
$ python3 -m timeit "import random" "list = ['1', '2', '3']" "choice = random.choice(list)
1000000 loops, best of 3: 1.92 usec per loop

Dictionaries are really cool - For author's future reference:
'Translating python dictionary to C++'
<http://stackoverflow.com/questions/1842941/translating-python-dictionary-to-c>

"""

# Note: Uses a Mersenne Twister as core generator
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def valid_choice(input_string, valid_string):
    if input_string.upper() not in valid_string or len(input_string) != 1:
        return False
    else:
        return True


def process_choice(input_string):
    if input_string.upper() == 'R':
        return 'rock'
    elif input_string.upper() == 'P':
        return 'paper'
    elif input_string.upper() == 'S':
        return 'scissors'
    elif input_string.upper() == 'Q':
        return 'quit'


while True:
    
    while True:

        print("""
        Enter your choice:
        R or r for rock
        P or p for paper
        S or s for scissors
        Q or q to quit
        """)

        user_choice = str(input())
        if not valid_choice(user_choice, "RPSQ"):
            clear_screen()
            print("Invalid input. Try again.")
            continue
        else:
            break

    user_choice = process_choice(user_choice)
    if user_choice == 'quit':
        break
    else:

        clear_screen()

        # Changed to tuple from list based on results; see header for details
        comp_tup = ('rock', 'paper', 'scissors')

        comp_choice = random.choice(comp_tup)
        print("Computer picked:  " + comp_choice)

        # key:value in this dictionary equivalent to winner:loser
        game_logic = {'rock': ['scissors'], 'paper': ['rock'], 'scissors': ['paper']}
        if user_choice == comp_choice:
            print("You tie against the computer")
        else:
            # if user_choice in game_logic[comp_choice]: checks if user is in losing position
            # Computer is always in winning position in this case (computer:user)
            # Therefore, computer is dominant and user loses
            if user_choice in game_logic[comp_choice]:
                print("You lose against the computer")
            # Otherwise, the user wins.
            else:
                print("You win against the computer")

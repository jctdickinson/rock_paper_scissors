"""
By JCT Dickinson
Using PyCharm Community Edition 5.0.4, TextMate 2.0-ß.8.5

14 Feb. 2016:
Pseudocode drawn up

15 Feb. 2016:
Terrible implementation of pseudocode completed with huge block of if statements

16 Feb. 2016:
Inclusion of dictionary that defines game logic allows for great simplification of program

17 Feb. 2016
Changed varible to store options for computer to a tuple for slight increase in efficiency

To do:
Make code more modular (functions).
Research difference between random.choice(), random.range(), and random.randint()
(used in previous magic8Ball project).
Include input validation (... why are try-excepts acceptable here in Python..?)

"""

# Note: Uses a Mersenne Twister as core generator
import random

# Note: while True seems to be the convention with Python 3+, as opposed to while 1.. for;; is completely foreign
while True:
    print("""
    Enter your choice:
    R or r for rock
    P or p for paper
    S or s for scissors
    Q or q to quit
    """)

    user_choice = input()

    if user_choice.upper() == 'R':
        user_choice = 'rock'
    elif user_choice.upper() == 'P':
        user_choice = 'paper'
    elif user_choice.upper() == 'S':
        user_choice = 'scissors'
    elif user_choice.upper() == 'Q':
        break

    comp_tup = ('rock', 'paper', 'scissors')
    # Below statement expressed as random choice within range:
    # comp_choice = comp_list[random.randint(0, 2)]
    # If choices are to be expanded, could also be expressed as
    # print("Computer picked:  " + randChoice[random.randint(0, len(randChoice)])
    # From what I can garner, choice() is moderately faster
    comp_choice = random.choice(comp_tup)
    print("Computer picked:  " + comp_choice)

    # For author's future reference:
    # 'Translating python dictionary to C++'
    # <http://stackoverflow.com/questions/1842941/translating-python-dictionary-to-c>
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
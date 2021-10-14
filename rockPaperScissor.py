# Huloooo!!!
# this is the code base for all the games
# rename this file when coding
# Khoda Hafiz <3
import random
print("r for rock \
          p for paper \
          s for scissor")
option = input("press y to start: ")

while(option == 'y'):
    user = input("your turn: ")
    computer = random.choice(['r', 's', 'p'])
    # r>s s>p P>r

    if (user == computer):
        print(f"computer's turn: {computer}")
        print("it's a tie!")
    elif (user == 'r' and computer == 's') or \
            (user == 's' and computer == 'p') or \
            (user == 'p' and computer == 'r'):
        print(f"computer's turn: {computer}")
        print("you won!!")
    else:
        print(f"computer's turn: {computer}")
        print("computer won!!")

    option = input("press y to play: ")




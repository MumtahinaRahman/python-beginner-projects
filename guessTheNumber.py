import random


def guess_the_number_comp():
    lower_bound = int(10)
    upper_bound = int(50)
    print(f"range : {lower_bound} to {upper_bound}")
    random_number = random.randint(lower_bound, upper_bound)
    guess = int(0)
    while guess != random_number:
        guess = int(input("input the number: "))
        if guess < random_number:
            print("oops!! Hint: go higher.")
        elif guess > random_number:
            print("oops!! Hint: go lower.")
        else:
            print(f"yay!! you guessed the number :){random_number}")
            break

def guess_the_number_hum():
    lower_bound = int(20)
    upper_bound = int(60)
    print(f"range : {lower_bound} to {upper_bound}")
    your_number = int(input("what's your secret number? :"))
    print("computer will guess your number.")
    print("press h to go higher and l for lower")
    guess = random.randint(lower_bound, upper_bound)
    hint = ""
    while your_number != guess:
        print(f"is this your number {guess}")
        hint = input("Hint: ")
        if hint == "h": #guess < your_number
            lower_bound = guess + 1
            guess = random.randint(lower_bound, upper_bound)
        elif hint == "l": #guess > your_number
            upper_bound = guess - 1
            guess = random.randint(lower_bound, upper_bound)

    if your_number == guess:
        print(f"woohoo!! computer guessed your number {your_number}")


print("what do you want to play?")
print("choose either of the games:")
print("1. computer has a secret number")
print("2. you have a secret number")
option = int(input("option: "))
if (option == 1):
    guess_the_number_comp()
else:
    guess_the_number_hum()
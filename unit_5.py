# written by oliver hamburger
# this program is a number guessing game

#imports random
import random

def get_random_number():
    """function gets a random number between 1 and 100"""
    r_number = random.randrange(1, 100)
    return float(r_number)


def game_loop(r_number):
    """loop that runs until you guess the correct number, it also counts the number of times
    you guess and if your guess was too high or too low"""
    count = 0
    while True:
        guess = int(input("pick a number between 1 and 100: "))
        if guess > r_number:
            print("your guess is to high")
            count +=1
        elif guess < r_number:
            count +=1
            print("your guess is to low")
        else:
            count +=1
            print("that is correct!, it took you",count,"guesses to get the answer" )
            break

def final():
    """function asks the user if they want to play again, then either end the program with a
    message or it runs the program again"""
    f = input("would you like to play again? (y/n): ")
    if f == "y":
        main()
    else:
        print("thanks for playing")


#function runs all other functions in order#
def main():
    I = input("would you like to guess my number? (y/n): ")
    if I == "y":
        r_number = get_random_number()
        game_loop(r_number)
        final()
    else:
         final()


main()












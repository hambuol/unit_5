# written by oliver hamburger
# this program is a number guessing game

import random

if input("would you like to guess my number? (y/n): ") == "y":
    def get_random_number():
        r_number = random.randrange(1, 100)
        return r_number

    def game_loop():
        while True:
            guess = input("pick a number between 1 and 100: ")




else:
    print("thanks for playing")












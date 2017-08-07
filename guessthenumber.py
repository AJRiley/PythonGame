#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1


name = input("Hello, What is your username?")

print("Hello", name + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("oh..okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
guess = int(input("Have a guess: "))
if guess > number:
    print("Guess lower...")
if guess < number:
    print("Guess higher..")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess Higher...")
    if guess > number:
        print("Guess Lower...")
if guess == number:
    print("You're right! you win! The number was {0} and it only took you {1} tries".format(number, tries))

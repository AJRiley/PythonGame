#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1


name = input("Hello, What is your username?")

print("Hello", name + ".", )

question = input("Would you like to play a game? [y/n] ")
if question == "n":
    print("Oh...okay")

if question == "y":
    print("I'm thinking of a number between 1 and 10")
guess = int(input("Take a guess: "))
if guess > number:
    print("Guess lower...")
if guess < number:
    print("Guess higher..")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess higher...")
    if guess > number:
        print("Guess lower...")
if guess == number:
    print("You win! The number was {0} and it only took you {1} tries!".format(number, tries))

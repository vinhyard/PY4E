#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
import math
line = input('Enter number: ')
while line == int or line == float:
    try:
        float(line)
        total = sum(line)
        print(total)
    except:
        print('You fucked up')

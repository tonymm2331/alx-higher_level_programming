#!/usr/bin/python3

import random

# Generate a random signed number between -10000 and 10000

number = random.randint(-10000, 10000)


# Print the randomly generated number
print("The number is:", number)


# Check if the number is greater than 0, equal to 0 or less than 0

if number > 0:
    print("is positive")

elif number == 0:
    print("is zero")

else:
    print("is negative")

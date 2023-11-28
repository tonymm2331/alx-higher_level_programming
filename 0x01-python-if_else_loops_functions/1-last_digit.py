#!/usr/bin/python3


import random

# Genarate a random number between -10000 and 10000

number = random.randint(-10000, 10000)

# Print thr randomly generated number
print("The string last digit of", number, "is", end=" ")

# Extaract the last digit of the number
last_digit = abs(number) % 10

# Print the last digit
print(last_digit, end=" ")

# Check if the last digit is greater than 5, equal to 0, or less than 6 and not 0
if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is 0")

else:
    print("and is less than 6 and not 0")

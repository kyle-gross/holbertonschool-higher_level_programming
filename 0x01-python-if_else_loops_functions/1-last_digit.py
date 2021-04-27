#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, end=" ")
print("is", end=" ")
if number < 0:
    number = -number
    last_digit = number % 10
    last_digit = -last_digit
else:
    last_digit = number % 10
if last_digit == 0:
    print(last_digit, "and is 0")
elif last_digit > 5:
    print(last_digit, "and is greater than 5")
else:
    print(last_digit, "and is less than 6 and not 0")

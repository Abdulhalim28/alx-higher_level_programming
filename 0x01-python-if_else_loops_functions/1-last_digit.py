#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {abs(number)%10} and is {'greater than 5' if abs(number)%10>5 else '0' if abs(number)%10==0 else 'less than 6 and not 0'}"}
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\ language that combines remarkable power with very clear syntax"
words = str.split()
print(*words[:4], end=" ")
print("with", end=" ")
print(*words[5:])



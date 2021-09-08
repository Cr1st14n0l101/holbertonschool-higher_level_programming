#!/usr/bin/python3
for i in range(25, -1, -1):
    character = i + ord('A')
    if i % 2 == 1:
        character += 32
    print("{:c}".format(character), end="")

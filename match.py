#!/usr/bin/env python3

# Using the 'match' statement in Python 3.10
# Docs: https://www.python.org/dev/peps/pep-0622/
# 
# This is a simple example of using the 'match' statement.


def validate_key(event) -> [int]:
    match event:
        case 'Left':
            return [1, 0]
        case 'Right':
            return [-1, 0]
        case 'Up':
            return [0, -1]
        case 'Down':
            return [0, 1]
        case _:  # 'default' case
            return [0, 0]


print('Match statement expression in Python 3.10:\n')
for key in ['Left', 'Right', 'Up', 'Down', 'foo']:  # Valid keys in console
    print(f"{key}: {','.join([str(val) for val in validate_key(key)])}")

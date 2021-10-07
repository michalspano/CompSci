"""
Recusrion in Python
"""


# Declare a recursive function
def recursive_function(i: int):
    if i > 0:
        print(f'I am being recursively called {N - i + 1} times.')
        recursive_function(i - 1)


# Fix contant recusrion range
N: int = 10
recursive_function(i=N)  # {Default recursion invoke}

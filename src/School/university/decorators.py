import time
import sys


# Create a decorator that prints the execution time of a function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start:.8}')
        return result
    return wrapper


# Create a decorator to estimate the size of a function
def estimate_size(func):
    def wrapper(*args, **kwargs):
        size = sys.getsizeof(func(*args, **kwargs))
        print(f'Size: {size}')
        return func(*args, **kwargs)
    return wrapper


# Create a decorator to turn console output to blue color
def blue_print(func):
    def wrapper(*args, **kwargs):
        print('\033[94m' + func(*args, **kwargs) + '\033[0m')
        return func(*args, **kwargs)
    return wrapper


@timeit
@estimate_size
def foo(N: int = 1000):
    for i in range(N):
        pass


@blue_print
def bar():
    return 'Hello World!'


foo()
bar()

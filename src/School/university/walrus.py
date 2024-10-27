# The walrus operator in Python (>=3.8)
# This way, we can assing a return of a function to a variable in a
# conditional statement, for loop, etc.

def foo(x, y) -> int:
    return x + y


def bar(x, y) -> int:
    return x * y


def main() -> None:
    '''
    Indeed, the multiple of two non-negative number is always greater than 
    the sum of two numbers (unless either is zero or one).
    '''
    
    # conditional statement
    if (n := foo(2, 3)) < (m := bar(2, 3)): # the beauty of the walrus operator B-)
        print(f'{n} is smaller than {m}')
    
    # for loop
    for i in range(n := foo(2, 3)):
        print(i, end=' ')
    print()

    # function call
    print(foo(n := foo(2, 3), m := bar(2, 3)))

    # lambda expression
    print((lambda x, y: x * y)(n := foo(2, 3), m := bar(2, 3)))

    # augmented assignment
    n = 0
    n += (m := bar(2, 3))

    # class definition
    class Foo:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.z = (n := foo(x, y)) ** (m := bar(x, y))
    
    print(Foo(2, 3).z)


if __name__ == '__main__':
    main()


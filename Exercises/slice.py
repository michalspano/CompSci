import random as r


# Create a random list
n: list = [chr(r.randint(65, 90)) for _ in range(20)]


def main():

    # Create a bool to store odd values
    isOdd: bool = True

    x: list = sliced_list(switch=isOdd)
    y: list = sliced_list()

    # Print out to console
    print(" ".join(x))
    print(" ".join(y))


def sliced_list(switch=False) -> list:

    # 'X', 'Y' of type list (even and odd elements) -> using slices
    # Using a switch to distinguish between types
    if switch:
        return n[::2]
    else:
        return n[1::2]


if __name__ == '__main__':
    main()

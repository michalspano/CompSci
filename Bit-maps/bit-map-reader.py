"""
Bit-map reader in Python
"""


def main():
    # Use command line arguments
    from sys import argv

    # Check for valid usage
    if len(argv) != 2:
        exit("Incorrect usage")

    # Store the binary sequence (of type string), skipping headers
    binary_sequence: str = [row.strip() for row in open(argv[1])][2:][0]

    # Set a constant intent (using 8 spaces), Range: <0-127>
    INTENT = 8

    # Iterate over the binary message (individual chars)
    message: str = ''
    for i in range(0, len(binary_sequence), INTENT):

        """
        SLICE in Python
        a[start:stop] : start->stop - 1
        a[slice(start, stop)]
        """

        # Convert each 8 bits from binary to ascii
        row = chr(int(binary_sequence[slice(i, i + INTENT)], 2))
        message += row

    # Print out the final message
    print(f"Encrypted message: {message!r}")


if __name__ == '__main__':
    main()

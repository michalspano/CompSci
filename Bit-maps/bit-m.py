"""
Bit maps
"""


# Create main function
def main():

    # Use command-line arguments to get file path
    from sys import argv

    # Check for valid number of command-line arguments
    if len(argv) != 2:
        exit("Usage: python[3] bit-m.py $OUTPUT_PATH [un-prefixed]")

    output_path = argv[1]

    # Get user input
    user_msg: str = input("Message: ")

    # Transform text message to binary
    binary_set: list = [bin(ord(char))[2:] for char in user_msg]

    # Open output text file (of type 'bmp', bitmap)
    output = open(f"{output_path}.pbm", "w")
    text_output = open(f"{output_path}.txt", "w")

    """
    Understanding 'Bitmaps'
    Source: https://en.wikipedia.org/wiki/Netpbm
    
    *****
    
    Define the bitmap header
    ln[0]: Portable BitMap 'P1'
    ln[1]: $WIDTH $HEIGHT
    """

    WIDTH, HEIGHT = 8, len(binary_set)
    header = f"P1\n{WIDTH} {HEIGHT}\n"
    output.write(header), text_output.write(header)

    # Store full sequence of type str
    binary_sequence: str = ''

    # Iterate over each row
    for row in binary_set:

        # Detect missing 0 (in the beginning)
        n = WIDTH - len(row)
        binary_sequence += "0" * n

        # Iterate over all chars in a row
        for char in row:

            # Assign chars to cont
            binary_sequence += char

    # Write the sequence to txt file and close it
    output.write(binary_sequence), text_output.write(binary_sequence)
    output.close(), text_output.close()

    # ***** OPTIONAL - COSMETIC *****
    import pandas as pd
    df = pd.DataFrame(data=binary_set, columns=['binary'], index=[i + 1 for i in range(len(binary_set))])
    print("\n"*3, df)


# Call the main function
if __name__ == '__main__':
    main()

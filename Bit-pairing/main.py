"""
Michal Špano
Bit pairing in Python
26/09/2021
"""

"""
Input:
8x8 [bit] = 1 BYTE
"""

# Declare default parity container
parity: list = [[None, None] for _ in range(8)]
diagonal_parity: list = [[None, None] for _ in range(15)]
# {13 parity valid diagonals + 2 empty (type None) * 2}


# Define main function
def main(PATH):
    global parity  # {Global parity reference}
    table: list = read_input(PATH)
    
    # Compute horizontal sequence from input
    row_sequence(table)

    # Compute vertical sequence (Columns)
    column_sequence(table)

    # Compute diagonal sequence from input
    diagonal_sequence(table)

    """
    Nested loop comprehension (structure):
    element for sublist in list for element in sublist ('element' is to be assigned)
    [Firstly, parse sublist and then iter in sublist]
    """

    # Print out parsed data
    print(f"Rows and columns:\n\n{' '.join(str(p) for sublist in parity for p in sublist)}")
    print(f"Diagonals:\n\n{' '.join(str(p) for sublist in diagonal_parity for p in sublist)}")


# Read input to a nested list
def read_input(PATH) -> list:
    return [row.strip().split() for row in open(PATH)]  # {Return formatted list}


# Define a function to compute row values
def row_sequence(input_sequence: list):
    global parity  # {Global reference}
    i: int = 0
    for row in input_sequence:
        counter: int = 0
        for value in row:  # {Iterate over all values in the sequence}
            if value == '1':
                counter += 1
        # Check if counter is even -> even parity
        state = parity_check(counter)  # {Invoke parity evaluation}
        # Assign value type bool
        parity[i][0] = state
        i += 1


# Define a function to compute column values
def column_sequence(input_sequence: list):
    global parity  # {Global reference}
    i: int = 0
    while i < len(input_sequence):
        counter: int = 0
        for j in range(len(input_sequence)):
            value = input_sequence[j][i]  # {Value - every i-th val. from j iterations}
            if value == '1':
                counter += 1
        # Check for even bit parity
        state = parity_check(counter)  # {Invoke parity evaluation}
        # Assign type bool
        parity[i][1] = state
        i += 1


# Define a function to compute diagonal values
def diagonal_sequence(input_sequence: list):
    global diagonal_parity  # {Assigning type bool or None}

    """
    Parity determined by at least 2 elements, otherwise type None
    """

    # Section 1 (diminishing line)
    for k in range(len(input_sequence) - 1):
        n: int = 0
        counter: int = 0
        for j in range(k, len(input_sequence)):
            value = input_sequence[j][n]
            if value == '1':
                counter += 1
            n += 1
        state = parity_check(counter)  # {Invoke parity evaluation}
        diagonal_parity[k][0] = state

    for k in range(1, len(input_sequence) - 1):
        i: int = k
        counter: int = 0
        for j in range(len(input_sequence) - k):
            value = input_sequence[j][i]
            if value == '1':
                counter += 1
            i += 1
        state = parity_check(counter)  # {Invoke parity evaluation}
        diagonal_parity[k + len(input_sequence) - 1][0] = state

    # Section 2 (increasing line)
    k = len(input_sequence) - 1
    while k >= 1:
        i: int = len(input_sequence) - (k + 1)
        counter: int = 0
        for j in range(len(input_sequence) - 1, len(input_sequence) - k - 2, -1):
            value = input_sequence[j][i]
            if value == '1':
                counter += 1
            i += 1
        state = parity_check(counter)
        diagonal_parity[len(input_sequence) - (k + 1)][1] = state
        k -= 1

    k = len(input_sequence) - 2
    while k >= 1:
        i: int = 0
        counter: int = 0
        for j in range(len(input_sequence) - 2 - (len(input_sequence) - 2 - k), -1, -1):
            value = input_sequence[j][i]
            if value == '1':
                counter += 1
            i += 1
        state = parity_check(counter)
        diagonal_parity[len(input_sequence) + (len(input_sequence) - 2 - k)][1] = state
        k -= 1


# Function to evaluate parity
def parity_check(count: int) -> bool:
    return True if count % 2 == 0 else False


# Invoke main function
if __name__ == '__main__':
    main('input.txt')

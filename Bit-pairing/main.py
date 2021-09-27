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
    p_o: tuple = diagonal_sequence(table)  # {Parity occurrence}
    output_parity: list = compute_diagonal_parity(p_o[0], p_o[1])

    """
    Nested loop comprehension (structure):
    element for sublist in list for element in sublist ('element' is to be assigned)
    [Firstly, parse sublist and then iter in sublist]
    """
    print("*** BIT PARITY ***\n'True' - Sequence has bit parity\n'False' - Invalid bit parity\n")

    # Print out parsed data
    print(f"Rows and columns:\n{' '.join(str(p) for sublist in parity for p in sublist)}")
    print(f'{len(parity)}x{len(parity)}\n')
    print(f"Diagonals:\n{' '.join(str(p) for sublist in output_parity for p in sublist)}")
    print(f'{len(output_parity)}x{len(output_parity)}')


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
def diagonal_sequence(input_sequence: list) -> tuple:

    """
    Parity determined by at least 2 elements, otherwise type None
    """
    diminishing_diagonal: list = []  # {Compute for the first section}
    increasing_diagonal: list = []  # {Compute for the second section}

    # Section 1 (diminishing line)
    for k in range(1, len(input_sequence) - 1):
        i: int = k
        counter: int = 0
        for j in range(len(input_sequence) - k):
            value = input_sequence[j][i]
            if value == '1':
                counter += 1
            i += 1
        state = parity_check(counter)  # {Invoke parity evaluation}
        diminishing_diagonal.append(state)

    # Refactor to the correct order (starting upwards)
    diminishing_diagonal.append(None)
    diminishing_diagonal = diminishing_diagonal[::-1]

    for k in range(len(input_sequence) - 1):
        n: int = 0
        counter: int = 0
        for j in range(k, len(input_sequence)):
            value = input_sequence[j][n]
            if value == '1':
                counter += 1
            n += 1
        state = parity_check(counter)  # {Invoke parity evaluation}
        diminishing_diagonal.append(state)
    diminishing_diagonal.append(None)

    # Section 2 (increasing line)
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
        increasing_diagonal.append(state)
        k -= 1

    # Refactor to the correct order (starting upwards)
    increasing_diagonal.append(None)
    increasing_diagonal = increasing_diagonal[::-1]

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
        increasing_diagonal.append(state)
        k -= 1
    increasing_diagonal.append(None)

    # Return both lists of occurrence
    return diminishing_diagonal, increasing_diagonal


# Function to evaluate parity
def parity_check(count: int) -> bool:
    return True if count % 2 == 0 else False


# Function to evaluate and format diagonal parity
def compute_diagonal_parity(d1: list, d2: list) -> list:
    global diagonal_parity  # {Global reference}
    for i in range(len(d1)):  # {Iterate over all instances}
        diagonal_parity[i][0] = d1[i]
        diagonal_parity[i][1] = d2[i]

    # Format 2 lists to a nested list
    return diagonal_parity


# Invoke main function
if __name__ == '__main__':
    main('input.txt')

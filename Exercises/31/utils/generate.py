# Generate source file for '31.py'
import random as r


# Function to generate new input file
def GENERATE(dimension: int, relate_path: str = 'in.txt'):
    output_file = open(relate_path, 'w')  # {Open input file}
    table: list[str] = create_hex_table()  # {Create hex table}
    output_file.write(f'{dimension} {dimension}\n')  # {Write file dimensions}
    for _ in range(dimension):
        row: str = ''
        for _ in range(dimension):  # {Iterate d times for each color of size 2 -> row * 2 x col}
            hex_code: str = ''.join([r.choice(table) for _ in range(2)])  # {Choose 2 random hex values}
            row += hex_code
        # Write each row to the text file
        output_file.write(f'{row}\n')
    output_file.close()  # {Close output}


# Create hex table with possible hex values
def create_hex_table() -> [str]:
    hex_table: list = [str(i) for i in range(10)]
    for i in range(6):
        hex_table.append(chr(i + 97))
    return hex_table

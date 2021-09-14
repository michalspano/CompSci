# This is a module to generate random names

# Import use libs
from typing import final
import random

# Create custom max to the size of a name
max_: final = 10

# Specify the fixed output path
output_file = open("src/names.csv", "w")

# Run in a desired loop
for _ in range(100):
    name: str = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(5, max_))])

    # Write to the output file
    output_file.write(f'{name}\n')

# Close text file
output_file.close()

"""
Michal Špano
14. Long Jump
21/09/2021
"""


# Define main function
def main():
    src_path: str = 'long_jump.txt'  # Define src path

    # Create a dict to store all data
    loaded_data: dict = {}

    # Open txt file from path
    with open(src_path) as input_file:
        i = 0
        for row in input_file:
            row = row.strip().split()
            loaded_data[f'competitor{i + 1}'] = {'name': row[0], 'country': row[1],
                                                 'jump': [int(row[i]) for i in range(2, len(row))]}
            i += 1

    # Data structure {{key1: value1, key2: value2, key3: [values3]}, ...}

    # Load countries from the dict
    countries = []
    for key in loaded_data:
        countries.append(loaded_data[key]['country'])

    # Create a dict counter for every competitor (and their country)
    j = 0
    countries_count: dict = {}
    for key in loaded_data:

        # Get current country
        country = loaded_data[key]['country']

        # Check for matching countries
        if countries[j] == country:
            # Assign dict key
            if country not in countries_count:
                countries_count[country] = 0

            # Increment key value
            countries_count[country] += 1
        j += 1

    # Print out the number of participants from each country
    for country in countries_count:
        print(f"{country}: {countries_count[country]}")

    # Load all the jumps in a list
    jumps: list = []
    for key in loaded_data:
        current_jumps: list = loaded_data[key]['jump']
        for j in current_jumps:
            jumps.append(j)

    print("\nWinner(s): ", end='')

    # Determine the winning jump
    max_jump: int = max(jumps)
    for key in loaded_data:

        # Load current jumps
        current_jumps = loaded_data[key]['jump']

        # Check if any other competitor reached the winning time
        if max_jump in current_jumps:

            # Print out the name(s)
            print(f"{loaded_data[key]['name']} ", end='')

    # Print out the best jump
    print(f": time: {max_jump}cm")


# Invoke main function
if __name__ == '__main__':
    main()

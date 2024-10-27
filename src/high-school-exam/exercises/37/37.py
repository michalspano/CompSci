#!/usr/bin/env python3
# Voting 2, EX. 37
# *** INF: Seminar ***

# ----8< Imports >8----
from sys import exit

# Create the main function
def main(PATH: str = 'voting_1.txt') -> None:
    # Open the input file
    data: list = [row.strip() for row in open(PATH, 'r')]

    # Reset text files
    for i in range(len(data)):
        f = open(f'{data[i]}.txt', 'w').close()

    # Mount in append mode
    for d in enumerate(data):
        idx: int = int(d[0]) + 1
        flag: str = d[1]
        current_file_name: str = f'{flag}.txt'
        try:
            with open(current_file_name, 'a') as f:
                f.write(f'{idx}\n')
                idx += 1
        # Handle the exception 
        except Exception as e:
            print(e)
            exit(1)
    print('Done!')
    exit(0)


# Call the main function
if __name__ == '__main__':
    main()


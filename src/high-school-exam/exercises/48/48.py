#!/usr/bin/env python3

"""
Michal Špano
48. Multiplication
06/11/2021
"""

# Import libs
import random as r


# Define main function
def main(out_path: str = 'out/multiplication.txt'):
    # Generate math problems
    data: list = generate_math_problems(OUT=out_path)
    # Final evaluation
    print(f'You got {solve_problems(data)} out of {len(data)} correct!')


# Function to generate 10 random multiplication problems
def generate_math_problems(LIMIT: int = 10, OUT: str = None) -> list:
    out_file = open(OUT, 'w')
    temp_data: list = []

    # Generate 10 random multiplication problems
    for _ in range(LIMIT):
        num1, num2 = r.randint(1, 10), r.randint(1, 10)
        temp_data.append([num1, num2, (num1 * num2), False])
        out_file.write(f'{num1} x {num2} = \n')

    # Close file and return
    out_file.close()
    return temp_data


# Function to solve the generated problems
def solve_problems(problems: list) -> int:
    count, round_count = 0, 0

    # Ask user for input until all are solved
    while not all(problem[-1] for problem in problems):

        # Iterate over all problems
        for i in range(len(problems)):

            # Skip over the math problem if it was already solved
            if problems[i][-1]:
                continue

            # Format console output
            print(f'Problem number {i + 1}: {problems[i][0]} x {problems[i][1]} = ', end='')

            # Get user input and check for correct type
            try:
                answer = int(input())
            except ValueError:
                print('Invalid input!')
                continue

            # Set state to True if answer is correct
            if answer == problems[i][2]:
                problems[i][-1] = True

                # Increment counter if guessed correctly for the first time
                if round_count < 1:
                    count += 1

        # Round counter
        round_count += 1

    # Return number of correct answers in the initial round
    return count


# Invoke main function
if __name__ == '__main__':
    main()

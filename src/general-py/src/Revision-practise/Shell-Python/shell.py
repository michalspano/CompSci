# Integrate Python with Shell script
import os


# Create the main function
def main():
    # Get the path of the shell script
    shell_path = input("Input path of the script: ")
    # Execute the shell script

    """
    Using 'os.system' to work as a bash command line 'sh' to execute a .sh file.
    Possible alternatives: 
    ./shell_path
    chmod +x shell_path
    ... 
    """

    execute_command(shell_path)


# Define a command executor function
def execute_command(path: str):
    os.system(f"sh {path}")
    """
    Possibly pass in the .sh path as a command line argument using:
    'from sys import argv'
    And iterate the argument vector.
    """


if __name__ == '__main__':
    main()

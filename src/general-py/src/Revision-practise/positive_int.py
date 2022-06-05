# Create a do-while loop

def main():
    # Print out the specified positive int
    print(f"{positive_int()} is a positive integer.")


# Promp the user for a positive integer
def positive_int():
    while True:
        # Get a user input (set to str by default)
        n = input("Input a positive integer: ")

        # Detect if digit was found
        if n.isdigit():

            # Convert n from type str to type int
            n = int(n)

            # Check validity of the numeric value
            if n > 0:
                break

    # Return the specified positive integer
    return n


# Create the main executable
if __name__ == "__main__":
    # Call the main function
    main()

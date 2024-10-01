"""
Michal Špano
5. Ordered Meals
09/09/2021
"""


# Define main function
def main():

    # Read from the text file
    with open("ordered_meals.txt") as input_file:
        read_data: list = [row.split() for row in input_file][1:]
        
    # 1. Print out the total number of ordered meals
    print(f"Number of ordered meals: {len(read_data)}\n")

    # 2. Count the number of individual meals
    # Store individual occurrence in a list
    meal_data: dict = {}
    for meal in read_data:
        prefix: str = meal[1]

        # Check whether current ID was not already passed
        if prefix not in meal_data:
            meal_data[prefix] = 0

        # Increment the counter of the current ID
        meal_data[prefix] += 1

    # Print the found occurrence from the dict
    for m in meal_data:
        print(f"{m} found {meal_data[m]} times.")

    # 3. Check for matching meal number (if lesser than 20 -> notify the user)
    print()
    MAX = 20

    # Iterate over the data set containing all meals
    for m in meal_data:
        count: int = meal_data[m]

        # Check for matching conditions
        if count < MAX:
            print(f"{m} ordered less than {MAX} times.")

        else:
            print(f"Is ready to be served!")


# Call the main function
if __name__ == '__main__':
    main()

# Import CSV library
import csv

from sys import exit


# Create a data set with question to ask the user
data_set = {
    "ID1": "name",
    "ID2": "age",
    "ID3": "city"
}


# Define the main function
def main():

    # Get the user input and assign it to a variable
    user_data = get_user_input()

    # Call the writer with the user data
    writer_function(user_data)


def get_user_input():

    # Create a list with use data
    csv_row = [input(f"{data_set[identifier]}: ") for identifier in data_set]

    # Return respective csv row
    return csv_row


def writer_function(data_row):

    # Open the CSV file
    with open("data.csv", "w") as inputCSV:

        # Define a csv writer
        csv_writer = csv.writer(inputCSV)

        # Write the row to the csv file
        csv_writer.writerow(data_row)


if __name__ == '__main__':
    
    # Call the main function
    main()
    exit(0)

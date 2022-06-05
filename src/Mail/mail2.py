"""
Database Reader
Michal Špano
11/09/2021
"""

# Create the main function
def main(d_name, d_ext):

    PATH = 'src/data_set.csv'
    # Declate a dict to store the values
    data_set: dict = {row.strip().split(';')[0]: row.strip().split(';')[1] for row in open(PATH).readlines()[1:]}

    # Print out mail addresses in the correct format
    for row in data_set:
        mail: str = f"{row}.{data_set[row]}@{d_name}.{d_ext}".lower()
        print(mail)


# Invoke main function
if __name__ == "__main__":
    main('abc', 'com')

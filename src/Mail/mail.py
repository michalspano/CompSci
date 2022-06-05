"""
Database Reader
Michal Špano
11/09/2021
"""

# Use lib. 'xlrd' to work with '.xls' files in Python
import xlrd

"""
Source: https://pypi.org/project/xlrd/
Structure: sheet_cell_val (rowx, colx)
"""

"""
Fix bad magic number:
https://github.com/Miserlou/Zappa/issues/854#issuecomment-313694177
"""


# Create main function (omiting command-line arguments)
def main(d_name, d_ext):

    # Locate and open the workbook
    workbook = xlrd.open_workbook("src/data_set.xls")

    # Open the sheet of index 0
    sheet = workbook.sheet_by_index(0)

    # Load all values to a dict
    data_set: dict = {(sheet.cell_value(row, 0).lower()):(sheet.cell_value(row, 1).lower()) for row in range(1, sheet.nrows)}

    # Output file (type .csv)
    output_file = open("dist/d_set_output.csv", "w")

    # Write initial header
    output_file.write('mail\n')

    # Display in a DataFrame (optional)
    from pandas import DataFrame
    arr: list = []

    # Iterate through elements in the dict
    for row in data_set:

        # Create mails with valid structure (all in lower case) and write it to the output file
        mail: str = f"{row}.{data_set[row]}@{d_name}.{d_ext}"
        output_file.write(f"{mail}\n")

        # Append to list
        arr.append(mail)

    # *** OPTIONAL ***
    df = DataFrame(data=arr, index=[i + 1 for i in range(len(arr))], columns=['mail'])
    print(df)

    # Close output file
    output_file.close()


# Main executable
if __name__ == '__main__':

    # Use predefined domain
    DOMAIN_NAME, DOMAIN_EXT = 'abc', 'com'
    main(DOMAIN_NAME, DOMAIN_EXT)

#!/usr/bin/env python3
# encoding: utf-8

from sys import exit
from pandas import read_excel
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def main():
    # Initialize Google Drive API
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # File credentials, TODO: considering to move to a config file
    # Include OWN file name
    file_name: str = 'foo.xlsx'

    # Include OWN file ID
    # File ID is found in the URL of the file in Google Drive, e.g.:
    # https://drive.google.com/d/<FILE_ID>
    file_ID: str = '123456789'

    # Create local file object
    file_obj = drive.CreateFile({'id': file_ID})
    file_obj.GetContentFile(f'{file_name}',
    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Format file to data structure
    data = read_excel(f'{file_name}', sheet_name='Form responses 1')
    data_dict = data.to_dict('records')

    ''' 
    Define data structure:
    [{response_1}, {response_2}, ... , {response_n}]
    '''

    # Hold column names in a list
    column_names: list = ['ID']  # Add new key value called 'ID', not found in the spreadsheet by default
    for key in data_dict[0].keys():
        column_names.append(key)

    try:
        if input("Operand: ").strip().lower() == 'csv':
            convert_to_plain_CSV('foo.csv', column_names, data_dict)

    except Exception as e:
        print(e)
        exit(1)


'''
Convert to plain .csv

Structure:
col_1;col_2;...;col_n
val_1;val_2;...;val_n
...
val_k+1;val_k+2;...;val_k+n

'''
def convert_to_plain_CSV(path: str, columns: list, data: list) -> None:
    with open(path, 'w', encoding='utf-16') as f:  # Use utf-16 to avoid encoding issues

        # Write column names
        f.write(';'.join(str(x) for x in columns) + '\n')

        # Assign IDs to responses
        idx: int = 1

        # Write following data
        for response in data:

            # Assign ID
            f.write(f'{idx};')

            for key in response:
                formatted_value: str = str(response[key]).replace('\n', ' ')

                # Avoid 'nan' values
                if formatted_value == 'nan':  # GS's default empty value
                    formatted_value = ''
                
                f.write(f'{formatted_value};')

            # Write new line for new response
            f.write('\n')

            # Increment ID number 
            idx += 1


if __name__ == '__main__':
    main()    
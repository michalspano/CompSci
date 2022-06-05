# Automated tool to convert link to pictorial qr code

import os
import qrcode

"""
'qrcode'
Source: https://pypi.org/project/qrcode/
"""

# Using command line arguments
from sys import argv, exit


# Main function
def main():

    # If command line argument was correctly specified
    if check_command_line_arg(argv):

        # Link of type str as the second argument
        link: str = argv[1]

        # Call the generator function
        qr_code_generator(link)
        exit(0)
    else:

        # Prompt the user with incorrect usage message
        print(f"Usage: python[3] {argv[0]} $LINK")
        exit(1)


def check_command_line_arg(args):

    # Check if 2 command line args were specified
    return False if len(args) != 2 else True


def qr_code_generator(link):

    """
    import qrcode
    img = qrcode.make('Some data here')
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
    """

    # Create qr-code
    img = qrcode.make(link)

    # Save the qr-code locally
    img.save("qr.png", "PNG")

    def open_qr_code():
        os.system("open qr.png")

    # Call a function to open the output in the system
    open_qr_code()


if __name__ == '__main__':
    main()

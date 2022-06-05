# Credits: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

import time, sys

class CLI:
    def display_colors():
        for i in range(0, 16):
            for j in range(0, 16):
                code: str= str(i * 16 + j)
                sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
            print (u"\u001b[0m")
            

    def display_colors_bg():
        for i in range(0, 16):
            for j in range(0, 16):
                code: str = str(i * 16 + j)
                sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
            print (u"\u001b[0m")


# Invoke the functions
CLI.display_colors(), print()
CLI.display_colors_bg()


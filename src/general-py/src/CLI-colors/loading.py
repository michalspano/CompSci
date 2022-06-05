#!/usr/bin/env python3

from sys import stdout
from time import sleep as s 


def main():
    loading()


def loading(timeInternval: float = 0.1, loadingSymbol: str = '#') -> None:

    ANSI_GREEN: str = '\033[32m'
    ANSI_RESET: str = '\033[0m'

    def clear_terminal_session() -> None:
        stdout.write("\033[2J\033[H")
    
    clear_terminal_session()

    # Range: <0;100>
    for i in range(100):
    
        # Delay the console for 'timeInternval' seconds
        s(timeInternval)
        width: int = (i + 1) // 4
        load: str = f"{i+1}%" 
        
        # Define current status of the loading bar in a string
        bar: str = f"[{ANSI_GREEN}{loadingSymbol * width}{' ' * (25 - width)}{ANSI_RESET}]"

        stdout.write(u"\u001b[1000D" + bar + load + ' ')
        
        # Reset the output buffer
        stdout.flush()
    print('\033[0m')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nHalt')
        exit(0)


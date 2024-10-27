#!/usr/bin/env python3

"""
Michal Špano
30. NIM12
Modified 12/10/2021
"""

import tkinter as tk
c_width, c_height = 650, 200
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()

# Global variables
player_match_draw: int = 0
player_match_count: int = 0
player1: bool = True


# Binding class (optional)
class Bind:
    # Initial constructor
    def __init__(self, ON, func):
        self.ON: bool = ON
        self.func: str = func

    # Bind/unbind click
    def button_click(self, ID: str = '<Button-1>'):
        canvas.unbind_all(ID) if not self.ON else canvas.bind_all(ID, eval(self.func))

    # Bind/unbind numeric input
    def keys(self, ID: str = '<Key>'):
        canvas.unbind_all(ID) if not self.ON else canvas.bind_all(ID, eval(self.func))


# Define main function
def main(N: int):
    # Draw matches N times
    [match(i * 45 + 10, 75, i + 1) for i in range(N)]
    print('Player 1 starts - pick number of moves: 1/2/3')

    # Initial keys bind
    Bind(True, 'remove_count').keys()
    canvas.mainloop()


# Function to draw a match tag: 'm-{i}'
def match(x: int, y: int, i):
    canvas.create_line(x, y, x, y + 100, width=5, fill='yellow', tags=f'm-{i}')
    canvas.create_oval(x - 5, y - 5, x + 5, y + 8,
                       fill='brown', outline='brown', tags=f'm-{i}')
    canvas.create_text(x + 3, y + 120, text=str(i), tags=f'm-{i}')


# Define a function to accept user click
def click(c):
    global player_match_count  # {Global reference}

    # Detect overlapping objects (i.e., objects below the cursor)
    overlap: tuple = canvas.find_overlapping(c.x - 3, c.y - 3, c.x + 3, c.y + 3)

    if len(overlap) > 0:  # {If any objects detected}
        if player_match_count < player_match_draw:  # {Remove counter boundary}
            """
            Receive default obj. tag form: 'm-{i}'
            'find_overlapping' detects only default canvas tags
            """
            obj_tag: str = canvas.gettags(overlap[0])[0]
            canvas.delete(obj_tag)  # {Delete selected match}

            # Detect if no more matches are left -> evaluate winner
            if end():
                Bind(False, 'remove_count').keys()
                show_winner()

            # Increment counter (except last draw)
            if player_match_count != player_match_draw - 1:
                player_match_count += 1

            # Bind/unbind options at last draw
            else:
                print('No more moves left.')
                Bind(False, 'click').button_click(), Bind(True, 'remove_count').keys()
                player_switch()  # {Switch players for next round}
                player_match_count = 0  # {Set to initial value}


# Detect player's number of removed matches
def remove_count(event):
    global player_match_draw  # {Global ref.}

    # Define possible keys
    keys: [str] = [str(i + 1) for i in range(3)]
    s_key: str = event.keysym

    # Detect valid key
    if s_key in keys:
        player_match_draw = int(s_key)  # {Update value}

        # Show current player
        print(f"{'Player 1' if player1 else 'Player 2'} - count: {player_match_draw}")

        # Bind/unbind
        Bind(False, 'remove_count').keys(), Bind(True, 'click').button_click()
    else:
        print('Invalid key.')


# Switch players
def player_switch():
    global player1
    player1 = False if player1 else True


# Detect end of the game
def end() -> bool:
    obj_count: int = len([ID for ID in canvas.find_all()])
    return True if obj_count == 0 else False  # {Number of objects is zero -> end}


# Show winner onto canvas
def show_winner():
    winner: str = 'Player 1' if player1 else 'Player 2'
    canvas.create_text(c_width / 2, c_height / 2, text=f'{winner} won!',
                       font='Helvetica 20 bold')


# Invoke main function
if __name__ == '__main__':
    main(15)

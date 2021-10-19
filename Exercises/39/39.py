#!/usr/bin/env python3

"""
Michal Špano
39. Customer satisfaction
19/10/2021
"""

# Libs
import tkinter as tk
from collections import Counter

# Instantiate a graphical canvas
c_width, c_height = 480, 520
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()


# Define main function
def main(src_path: str = 'satisfaction.txt'):
    # Sort satisfaction input to a dict
    # dist {'yes': [time_1, ... , time_n], 'no': [time_2, ... , time_n+1]}
    satisfaction_data: dict = {'yes': [], 'no': []}
    with open(src_path) as f:
        for row in f:
            r: list = row.strip().split()
            satisfaction_data[r[1]].append(r[0])

    # Total number of negatives comments, i.e. 'no'
    print(f"Number of negative comments: {len(satisfaction_data['no'])}\n")

    # An hour with the most dissatisfied customers
    hours: dict = Counter(time.split(':')[0] for time in satisfaction_data['no'])
    _max: list = max([int(hours[key]), key] for key in hours)
    print(f"The most dissatisfied customers appeared at: {_max[1]!r}"
          f"\nCount: {str(_max[0])!r}\n")

    # Dissatisfied customers for each hour
    for hour in hours:
        print(f"Number of dissatisfied customers: {hours[hour]}\nHour: {hour!r}")

    """
    Histogram in Tk
    480x520
    """

    s: int = 20  # {Fixed size of 1 chart element}

    # Display number lien
    def number_line():
        for i in range(24):
            canvas.create_text(s * i + 10, c_height - s, text=str(i))
        canvas.create_line(0, c_height - s - 10, c_width, c_height - s - 10, width=2)

    # Display individual chars data
    def chart_data():
        for h in hours:
            for i in range(hours[h]):
                canvas.create_rectangle(s * int(h), c_height - s - ((i + 1) * s),
                                        s * (int(h) + 1), c_height - s - ((i + 2) * s),
                                        fill='green')

    # Call methods
    number_line(), chart_data()


# Invoke main function
if __name__ == '__main__':
    main()
    canvas.mainloop()

#!/usr/bin/env python3

"""
Michal Špano
58. Subway Line
13/11/2021
"""

# Tkinter preferences
import tkinter as tk
c_width, c_height = 600, 400
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()

"""
Abstract:
    Create a subway line with stations and lines.
    Drawn with Tkinter.
"""


# Define the main function
def main(line_path: str = 'src/subway_line_route.txt'):
    loaded_data: tuple = load_route_data(line_path)

    # Check if valid hex color was provided
    if not is_valid_hex_color(loaded_data[0]):
        exit('Invalid hexadecimal color.')

    # Display route data onto a canvas
    display_route_data(*loaded_data)


# Create a function to load route data
def load_route_data(PATH) -> (str, dict):
    route_data: dict = {}  # {route data}

    # Open the input text file
    with open(PATH, 'r') as f:
        route_color: str = f.readline().strip()

        # Load individual station data
        for row in f:
            current_station: str = row.strip()

            # Skip redundant blank lines and EOF
            if current_station == '':
                continue

            # Distinguish between stations and and express stations (denoted with '*')
            if current_station[0] == '*':
                route_data[current_station[1:]] = True
            else:
                route_data[current_station] = False

    # Return (color;data)
    return route_color, route_data


# Function to display route data
def display_route_data(route_color: str, route_data: dict, pos_size: int = 7.5) -> None:
    # Display main line
    canvas.create_line(0, c_height // 2, c_width, c_height // 2, width=5, fill=route_color)

    # Determine the number of present stations
    number_of_stations: int = len(route_data)

    # Even spacing
    s: int = c_width // number_of_stations

    # Middle of the canvas
    mid_y: int = c_height // 2

    i: int = 0
    for key in route_data:
        # Create fixed coords for the station
        trail_x: int = i * s + 20
        station_coords: list = [trail_x - pos_size, mid_y - pos_size,
                                trail_x + pos_size, mid_y + pos_size]

        # Detect the first and the last stations (canvas type - rectangle)
        if i == 0 or i == number_of_stations - 1:
            canvas.create_rectangle(station_coords,
                                    fill=route_color)

        else:
            # Otherwise create default canvas objects
            # and change colors of express stations
            station_fill: str = '#ffffff' if route_data[key] else route_color
            canvas.create_oval(station_coords,
                               fill=station_fill)

        # Display stations' name
        canvas.create_text(trail_x + 20, mid_y - 100, text=key, angle=65)
        i += 1


# Function to determine valid hex color
def is_valid_hex_color(color: str) -> bool:
    if len(color) != 7:  # {valid length}
        return False
    if color[0] != '#':  # {valid format}
        return False
    for i in range(1, 7):  # {check valid hex digits; 1-9, a-f}
        if not color[i].isdigit() and not 'a' <= color[i].lower() <= 'f':
            print('a')
            return False
    return True


# Call main function
if __name__ == "__main__":
    main()
    canvas.mainloop()

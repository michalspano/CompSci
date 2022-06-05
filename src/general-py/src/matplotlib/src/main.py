#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @michalspano

import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from math import e as euler


# Define the main function
def main() -> None:
    # Define the number of command-line arguments; ensure usage
    if len(argv) != 2:
        print("Usage: ./main.py <n>")
        exit(1)

    # Ensure the number of command-line arguments is an integer
    try:
        r: int = int(argv[1])
    except ValueError:
        print("<n> must be an integer")
        exit(1)

    # Ensure positive values for <n>, greater than 1
    if r <= 1:
        print("<n> must be greater than 0")
        exit(1)

    # Define step size of the function
    step: int = 10

    # Compose x, y values in the given range
    x_points: np.array = np.array(
        [(i + 1) / step for i in range(r)]
    )
    y_points: np.array = np.array(
        [euler ** ((i + 1) / step) for i in range(r)]
    )

    # Plot the points
    plt.plot(x_points, y_points)

    # Compute mathematical expression with LaTeX
    plt.title(rf"$f(x)=e^x, x \in [0;{r / step}]$")

    # Show the plot
    plt.xlabel("x"), plt.ylabel("f(x)"), plt.show()


if __name__ == '__main__':
    main()

# Banking module

# Create the main function
def main():

    # Time module
    from datetime import datetime
    begin = datetime.now()

    # Let A, B, C be 3 different interest rates (A < B < C)
    a, b, c, = 1.5, 2.0, 2.5

    # We want to calculate in how many years the sum in a bank account will be equal or greater than 2000 (e)
    e: int = 2000

    # Initialize a counter to store all the counters
    counters: list = []

    # Iterate over all interest rates
    for rate in [a, b, c]:

        # Set initial sum an counter
        d: int = 1000
        counter: int = 0

        # Increment counter while value not matched
        while d % e >= d:
            d += (d / 100 * rate)
            counter += 1

        # Append the counter instance
        counters.append(counter)

    end = datetime.now()

    # ***** OPTIONAL - COSMETIC *****
    import pandas as pd

    df = pd.DataFrame(data=counters, index=[str(a) + '%', str(b) + '%', str(c) + '%'], columns=["years"])
    print(df)

    print(f"Time: {end - begin}")


# Invoke main function
if __name__ == "__main__":
    main()

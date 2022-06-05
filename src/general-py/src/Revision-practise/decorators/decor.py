# Decorators in Python

# Define main function
def main():
    # Call the decorated function
    have_beer()


# Define credentials to be used in the function
credentials = {
    "name": "Michal",
    "age": 18
}


# Create an adult check
def adult_check(func):
    def wrapper():
        if credentials['age'] >= 18:
            func(True)
        else:
            func(False)
    return wrapper


# Assign the decorator to the specific function
@adult_check
def have_beer(adult):
    if adult:
        print(f"{credentials['name']} can have a beer with us!")
    else:
        print(f"No beer for {credentials['name']}")


# Create a main executable
if __name__ == "__main__":
    main()

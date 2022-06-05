# ***For educational purposes only***

from sys import exit
from csv import DictReader


# Load CSV source file
def load_people(path: str = 's.csv') -> dict or None:
    temp: dict = {}
    # Catch invalid input file
    try:
        with open(path) as f:
            reader = DictReader(f)
            for person in reader:
                temp[person['name']] = int(person['age'])

        # Return the populated dictionary of people
        return temp

    # Return None if not found
    except FileNotFoundError:
        return None


people: dict = load_people()

# Check if the dict is not empty
if not people:
    print('No people found.')
    exit(1)


# Define a decorator that will check whether the person is an adult
# If so, return the function
# If not, return a message
def check_adult(func):
    def wrapper(*args, **kvargs):
        name: str = args[0]
        if people[name] >= 18:
            return func(*args, **kvargs)
        print(f'You have to wait {18 - people[name]} years to be an adult.')
    return wrapper


@check_adult  # Assigning the decorator
def grab_beer(name: str):
    print(f'Have a beer with us, {name}!')


# Iterate over all people
for name in people:
    grab_beer(name)


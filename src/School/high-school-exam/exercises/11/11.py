"""
Michal Špano
11. Foot Race
20/09/2021
"""


# Define main function
def main():
    src_path: str = 'foot_race.txt'  # {Define path of source txt file}

    """
    File Format:
    'Name' 'Time [s]' '\n'
    """

    load_data: list = []  # {Load data to a list}

    with open(src_path) as input_file:
        for row in input_file:
            row = row.strip().split()
            load_data.append([int(row[1]), row[0]])

    # {Print out number of competitors}
    print(f"Number of competitors: {len(load_data)}\n")

    # {Print out all people}
    for person in load_data:
        print(f"Athlete {person[1]} reached the finish line in {person[0]} seconds.")

    # Define the winner
    fastest_competitor: list = min(load_data)
    print(f"\nFastest competitor {fastest_competitor[1]} reached finish line in ", end='')

    winner_t: int = fastest_competitor[0]  # {In seconds}

    print(f"{format_time(winner_t)}")  # {Formatted output}


# {Formats sec to min and sec (type str)}
def format_time(time_sec: int) -> str:
    time_min: int = 0

    while time_sec >= 60:
        time_sec -= 60
        time_min += 1

    return f"'{time_min} min. {time_sec} sec.'"


# Define main executable
if __name__ == '__main__':
    main()

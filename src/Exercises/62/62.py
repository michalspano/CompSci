#!/usr/bin/env python3

"""
Michal Špano
62. Survey
15/11/2021
"""


# Adjust canvas objects
import tkinter as tk
c_width, c_height = 600, 300
canvas = tk.Canvas(height=c_height, width=c_width)
canvas.pack()


# Function to load data from a file to memory
def load_data(path: str) -> [str, [int]] or None:
    try:  # {Handle exception with file error}
        with open(path) as f:
            try:  # {Handle exception with invalid file structure}
                return [f.readline().strip(), [int(i) for i in f.readline().split()]]
            except IndexError or ValueError:
                return None
    # Catch exception
    except FileNotFoundError:
        return None


# Draw the graph
def draw_bar(x: int, y: int, width: int, color: str, tag: str) -> None:
    canvas.create_rectangle(x, y - 15, x + width, y + 15, fill=color, tags=tag)


# Draw individual bars
def display_answer(x: int, y: int, answer: str, tag: str) -> None:
    canvas.create_text(x, y, text=answer, tags=(tag, 'stats'))


# Load initial data from file
src_path: str = 'survey.txt'
data = load_data(src_path)

# Handle None data
if data is None:
    exit('File not found or incorrect file structure.')

# Static data
colors: [str] = ['red', 'green']
possible_answers: [str] = ['Yes', 'No', 'Idk']
survey_question: str = data[0]

# Global dynamic reference
votes: [int] = data[1]


# Dynamic function
def max_votes(current_votes: list) -> int:
    return max(current_votes)


# Bind user_click to canvas left click
def user_click(event) -> None:
    global votes  # {Global list reference}
    cursor_overlap: tuple = canvas.find_overlapping(event.x, event.y, event.x, event.y)

    # Handle cursor overlap
    if not cursor_overlap or len(cursor_overlap) != 1:
        return
    # Parse valid, current object tag at cursor overlap
    tag: str = canvas.gettags(cursor_overlap[0])[0]

    # Increment vote for the corresponding answer
    try:
        votes[int(tag.split('-')[-1])] += 1
    except ValueError:
        print('Invalid object selected.')
        return

    # Update display
    display_assets()
    update_file(src_path)


# Function to display canvas objects
def display_assets() -> None:
    canvas.delete('all')
    canvas.create_text(c_width // 2, 20, text=survey_question, font=('Arial', 20))

    # Iterate over possible answers
    for i in range(len(votes)):
        current_vote: int = votes[i]

        # Detect distinct max vote color
        display_color: str = colors[0] if current_vote != max_votes(votes) else colors[1]

        # Draw bars for each answer in percentages
        draw_bar(150, i * 50 + 100, current_vote * 200 // max_votes(votes),
                 display_color, f'bar-{i}')

        # Display answer text with corresponding vote count
        display_answer(50, i * 50 + 100, f'{possible_answers[i]} - {current_vote}',
                       f'answer-{i}')


# Create a function to update text file
def update_file(path: str) -> None:
    with open(path, 'w') as f:
        f.write(survey_question + '\n')
        for i in votes:
            f.write(str(i) + ' ')
        f.write('\n')


# Create a function to reset votes in the text file
def reset_votes() -> None:
    global votes
    votes = [1] * len(possible_answers)
    update_file(src_path)
    display_assets()
    print('File data reset.')


display_assets()

# Bind user_click to canvas left click
canvas.bind_all('<Button-1>', lambda event: user_click(event))
print('Survey ready.\nPress answer to update it. ', end='')

# Biden space key to reset votes
canvas.bind_all('<space>', lambda event: reset_votes())
print('Press space to reset votes.')
canvas.mainloop()

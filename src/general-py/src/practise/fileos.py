#!/usr/bin/env python3
import os

# Find all directories from the base directory
def find_dir(base_dir: str) -> list:
    dir_list: list = []
    for item in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, item)):
            dir_list.append(item)
    return dir_list


# Find all files from the base directory
def find_file(base_dir: str) -> list:
    file_list: list = []
    for item in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, item)):
            file_list.append(item)
    return file_list


# Print all dirs in the current path
PATH: str = os.getcwd()
print(f"All directories {' '.join(find_dir(PATH))}")
print(f"All files {' '.join(find_file(PATH))}")


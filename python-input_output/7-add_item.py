#!/usr/bin/python3


"""
This script adds all command-line arguments to a Python list and saves them 
to a file named 'add_item.json'.

It uses the `save_to_json_file` function from the module 5-save_to_json_file.py 
to save the list and `load_from_json_file` from 6-load_from_json_file.py to load 
the existing list from the file if it exists.
"""

from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load the existing list, or initialize an empty list if the file doesn't exist
try:
    current_list = load_from_json_file(filename)
except FileNotFoundError:
    current_list = []

# Add all arguments (except the script name) to the list
current_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(current_list, filename)

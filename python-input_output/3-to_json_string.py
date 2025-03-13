#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    Args:
        my_obj: The object to be serialized to JSON.
    
    Returns:
        str: JSON representation of the input object.
    """
    return json.dumps(my_obj)


# Test cases to ensure the function works with different inputs

# Case 1: A list of numbers and a string
data = [1, 2, 3, "Holberton"]
print(to_json_string(data))  # Expected: '[1, 2, 3, "Holberton"]'

# Case 2: An empty list
data = []
print(to_json_string(data))  # Expected: '[]'

# Case 3: A dictionary with one key-value pair
data = {'id': 12}
print(to_json_string(data))  # Expected: '{"id": 12}'

# Case 4: A dictionary with multiple keys and a list as a value
data = {'id': 12, 'numbers': [1, 2, 4]}
print(to_json_string(data))  # Expected: '{"id": 12, "numbers": [1, 2, 4]}'

# Case 5: A big dictionary
data = {
    'id': 123456,
    'name': 'Test',
    'info': {
        'details': 'This is a large dictionary example',
        'values': [100, 200, 300],
        'nested_dict': {'key': 'value'}
    }
}
print(to_json_string(data))  # Expected: JSON string of the large dictionary

# Case 6: A big list of dictionaries
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'}
]
print(to_json_string(data))  # Expected: JSON string of the list of dictionaries

# Case 7: A simple string
data = "Simple string"
print(to_json_string(data))  # Expected: '"Simple string"'

# Case 8: Invalid data format (incorrect dictionary)
try:
    data = {'id': 3, 'title': "Holberton", 89}  # Invalid data: missing key for 89
    print(to_json_string(data))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Expected: exception about the invalid dictionary

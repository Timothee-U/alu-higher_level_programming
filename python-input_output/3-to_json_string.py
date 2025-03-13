#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    This function takes an object as input and converts it to a JSON string
    using the json.dumps() method. It is intended to handle any object that
    can be serialized to JSON.

    Args:
        my_obj (object): The object to be serialized to JSON.
    
    Returns:
        str: The JSON string representation of the input object.
    
    Example:
        >>> to_json_string([1, 2, 3])
        '[1, 2, 3]'
        
        >>> to_json_string({'name': 'Alice', 'age': 25})
        '{"name": "Alice", "age": 25}'
    """
    return json.dumps(my_obj)

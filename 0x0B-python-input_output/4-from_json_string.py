#!/usr/bin/python3
"""
4-from_json_string Module has 1 function:
    from_json_string()
"""


def from_json_string(my_str):
    """
    Retruns a Python object represented by a JSON string..

    Args:
        my_str (string): string to deserialize.

    Return:
        Python object representation of the JSON string 'my_str'.
    """

    import json

    return json.loads(my_str)

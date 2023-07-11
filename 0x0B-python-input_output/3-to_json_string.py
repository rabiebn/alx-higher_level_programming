#!/usr/bin/python3
"""
3-to_json_string Module has 1 function:
    to_json_string()
"""


def to_json_string(my_obj):
    """
    Retruns the JSON representation of an object (string).

    Args:
        my_obj (Any): object to serialize.

    Return:
        JSON string representation of 'my_obj'.
    """

    import json

    return json.dumps(my_obj)

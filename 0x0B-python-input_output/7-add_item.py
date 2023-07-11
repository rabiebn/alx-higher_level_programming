#!/usr/bin/python3
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    args = list(load_from_json_file(filename))
except Exception as e:
    args = []
finally:
    for arg in sys.argv[1:]:
        args.append(arg)

    save_to_json_file(args, filename)

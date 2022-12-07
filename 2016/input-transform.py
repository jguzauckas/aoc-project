import json

# Read information out of file into list
with open("2016/input.txt", "r") as input_file:
    input_str: str = input_file.readline()

# Create list of smaller strings instead of a string
input: list[str] = input_str.split(", ")

# Put into "input.json" file for use in puzzle solving program!
with open("2016/input.json", "w") as my_file:
    json.dump(input, my_file)

import json

# Read information out of file into list
with open("2017/input.txt", "r") as input_file:
    input_str: str = input_file.readline()

# Create list of characters instead of a string
input: list[int] = []
for character in input_str:
    input.append(int(character))

# Put into "input.json" file for use in puzzle solving program!
with open("2017/input.json", "w") as my_file:
    json.dump(input, my_file)

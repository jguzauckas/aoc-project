import json

# Read information out of file into list
with open("2018/input.txt", "r") as input_file:
    input: list[str] = input_file.readlines()

# Strip newline characters from input
for pos, item in enumerate(input):
    input[pos] = item.strip()

# Put into "input.json" file for use in puzzle solving program!
with open("2018/input.json", "w") as my_file:
    json.dump(input, my_file)

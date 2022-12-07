import json

# Read information out of file into list
with open("2020/input.txt", "r") as input_file:
    input_str: list[str] = input_file.readlines()

# Strip newline characters from input
for pos, item in enumerate(input_str):
    input_str[pos] = item.strip()

# Re-read as integers
input: list[int] = []
for item in input_str:
    input.append(int(item))

# Put into "input.json" file for use in puzzle solving program!
with open("2020/mrg-input.json", "w") as my_file:
    json.dump(input, my_file)

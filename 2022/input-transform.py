import json

# Read information out of file into list
with open("input.txt", "r") as input_file:
    input_str: list[str] = input_file.readlines()

# Strip newline characters from input
for pos, item in enumerate(input_str):
    input_str[pos] = item.strip()

# Create list of integers instead of strings
input: list[int] = []
for num in input_str:
    if num == "":
        input.append(-1)
    else:
        input.append(int(num))

# Put into "input.json" file for use in puzzle solving program!
with open("input.json", "w") as my_file:
    json.dump(input, my_file)
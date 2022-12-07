import json

# Read information out of file into list
with open("2016/input.txt", "r") as input_file:
    input_str: str = input_file.readline()

# Create list of smaller strings instead of a string
input: list[str] = input_str.split(", ")

# Put into "input.json" file for use in puzzle solving program!
with open("2016/mrg-input.json", "w") as my_file:
    json.dump(input, my_file)

direction = 0
x = 0
y = 0
coords = [(0, 0)]
first = tuple()
for inp in input:
    if inp[0] == "L":
        direction -= 1
    else:
        direction += 1
    if direction % 4 == 0:
        y += int(inp[1:])
    elif direction % 4 == 1:
        x += int(inp[1:])
    elif direction % 4 == 2:
        y -= int(inp[1:])
    else:
        x -= int(inp[1:])
    for coord in coords:
        if x == coord[0] and y == coord[1] and first == ():
            first = coord
    coords.append((x, y))
print(x)
print(y)
print(abs(x) + abs(y))
print(first)

tup = tuple()

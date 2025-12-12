

# Set initial variables
DIAL_POSITION = 50
DIAL_MAX = 99
DIAL_MIN = 0

zero_counter = 0
dial_moves = []
multiplier = 0

# Read lines from input file and replace L's with - and R's with nothing
# Append the int to the dial_moves list
with open("Day01/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("L", "-")
        line = line.replace("R", "")
        dial_moves.append(int(line))

# iterate over the list of dial moves to update the dial position
for move in dial_moves:
    DIAL_POSITION = DIAL_POSITION + move
    if DIAL_POSITION > 99 or DIAL_POSITION < 0:
        multiplier = divmod(DIAL_POSITION, 100)[0]
        DIAL_POSITION = DIAL_POSITION - (100 * multiplier)

    # if the dial landed on zero, increment the counter by 1
    if DIAL_POSITION == 0:
        zero_counter += 1

print(zero_counter)

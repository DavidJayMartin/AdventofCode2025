

# Set initial variables
dial_position = 50
zero_counter = 0

# Read lines from input file and create list of dial moves [direction, turn distance]
with open("Day01/input.txt", "r") as f:
    lines = f.readlines()

moves = [(move[0], int(move[1:])) for move in lines]

# iterate over the list of dial moves
for move in moves:
    
    # cycle through full dial rotations and count the tiems past zero
    zeros, rotation = divmod(move[1], 100)
    zero_counter += zeros

    # if turning to the right and if the initial position
    # plus the dial move is >= 100, increment counter
    if move[0] == "R":
        if dial_position + rotation >= 100:
            zero_counter += 1
        
        # update the dial position
        dial_position = (dial_position + rotation) % 100
    
    # if turing to left,  and if the initial position
    # minus the dial move is <= 100, increment counter
    else:
        if dial_position and dial_position - rotation <= 0:
            zero_counter += 1
        
        # update the dial position
        dial_position = (dial_position - rotation) % 100

print(zero_counter)
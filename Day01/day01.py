

# Set initial variables
dial_position = 50
zero_counter = 0

# Read lines from input file and replace L's with - and R's with nothing
# Append the int to the dial_moves list
with open("Day01/input.txt", "r") as f:
    lines = f.readlines()

moves = [(move[0], int(move[1:])) for move in lines]

# iterate over the list of dial moves to update the dial position
for move in moves:
    
    zeros, rotation = divmod(move[1], 100)
    zero_counter += zeros

    if move[0] == "R":
        if dial_position + rotation >= 100:
            zero_counter += 1
        dial_position = (dial_position + rotation) % 100
    else:
        if dial_position and dial_position - rotation <= 0:
            zero_counter += 1
        dial_position = (dial_position - rotation) % 100

print(zero_counter)



    # # save the last position and move the dial
    # last_position = dial_position
    # dial_position = dial_position + move

    # # check if the dial is > 100 away from zero
    # # count the full turns of the dial
    # # reset the dial_position to a number in the valid range
    # if dial_position > 99 or dial_position < -99:
    #     multiplier = divmod(dial_position, 100)[0]
    #     zero_counter += abs(multiplier)
    #     dial_position = dial_position - (100 * multiplier)

    # # the dial stayed within 100 of zero
    # # check if there was a sign change or if it landed on zero   
    # else:
    #     if dial_position == 0:
    #         zero_counter += 1
    #     if (dial_position > 0 and last_position < 0) or (dial_position < 0 and last_position > 0):
    #         zero_counter += 1

    #     # move the dial back to the valid range
    #     if dial_position < 0:
    #         dial_position = dial_position + 100

# set initial variables
text= ""
seq = []
invalid_nums = []
total = 0

# read in the sequences from the file
# split them and add them to a list
with open("Day02/input.txt", "r") as f:
    text = f.read()
    seq = text.split(",")

for num in seq:
    num_list = num.split("-")

    start = int(num_list[0])
    end = int(num_list[1]) + 1

    for n in range(start,end):
        if len(str(n)) % 2 == 0:
            div = int((len(str(n))/2))
            if str(n)[:div] == str(n)[div:]:
                invalid_nums.append(n)

for invalid in invalid_nums:
    total += invalid

print(total)

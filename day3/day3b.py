"""
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left
corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these
produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

Your puzzle answer was 7560370818.
"""

inputfile = 'input.txt'
slopes = [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]     # List of different trajectories to use


def sledtheslope(map, slope):
    row = 0
    col = 0
    treecount = 0
    dx = slope[0]
    dy = slope[1]

    while row < len(map):
        # print(f'Sledding at ({row},{col}) -> \'{map[row][col]}\'')
        if map[row][col] == '#':
            treecount += 1
        col = (col + dx) % len(entries[row])
        row += dy
    return treecount


fp = open(inputfile, 'r')
entries = fp.read().splitlines()
counts = []
product = 1

for slope in slopes:
    mycount = sledtheslope(entries, slope)
    counts.append(mycount)
    print(f'Encountered {mycount} trees with slope {slope}')
for count in counts:
    product *= count
print(f'Final product = {product}')


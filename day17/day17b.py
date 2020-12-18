"""
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy source engineers expected.
Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w),
there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ
by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at
x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules
for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional,
this initial state represents a small 2-dimensional slice of it.
(In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle
is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....
After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space.
How many cubes are left in the active state after the sixth cycle?

Your puzzle answer was 1524.
"""
from copy import deepcopy
from datetime import datetime

entries = []
fname = "input.txt"
outerlimit = 20

print(f'Starting execution at {datetime.now()}')

def num_neighbors_active(coord, universe):
    # coord is a list of four integers [x,y,z,w]
    active = 0
    x = coord[0]
    y = coord[1]
    z = coord[2]
    w = coord[3]
    for xi in range(-1, 2):
        for yi in range(-1, 2):
            for zi in range(-1, 2):
                for wi in range(-1, 2):
                    try:
                        if universe[x+xi][y+yi][z+zi][w+wi] == '#':
                            active += 1
                    except IndexError:
                        pass
    if universe[x][y][z][w] == '#':
        active -= 1
    return active


space = []
# Seed space
for x in range(0, outerlimit):
    space.append([])
    for y in range(0, outerlimit):
        space[x].append([])
        for z in range(0, outerlimit):
            space[x][y].append([])
            for _ in range(0, outerlimit):
                space[x][y][z].append('.')


with open(fname, 'r') as fp:
    for line in fp:
        entries.append(line.strip())
print(entries)

mp = int((outerlimit - len(entries[0])) / 2)
xs = ys = mp
ws = zs = int(outerlimit / 2)

for entry in entries:
    xs = mp
    for bit in entry:
        # print(f'Seeing bit: {bit} going to {xs},{ys},{zs},{ws}')
        space[xs][ys][zs][ws] = bit
        xs += 1
    ys += 1

icount = 0
while icount < 6:
    print(f'{datetime.now()} Iteration # {icount}')
    newspace = deepcopy(space)
    for w in range(0, outerlimit):
        for z in range(0, outerlimit):
            for y in range(0, outerlimit):
                for x in range(0, outerlimit):
                    numneighbors = num_neighbors_active([x, y, z, w], space)
                    if space[x][y][z][w] == '.' and numneighbors == 3:
                        newspace[x][y][z][w] = '#'
                    elif space[x][y][z][w] == '#' and (numneighbors == 2 or numneighbors == 3):
                        newspace[x][y][z][w] = '#'
                    else:
                        newspace[x][y][z][w] = '.'
    space = deepcopy(newspace)
    icount += 1

activecount = 0
for surf in space:
    for row in surf:
        for hyper in row:
            activecount += hyper.count('#')

print(f'program complete at {datetime.now()}')
print(f'Number of active cells = {activecount}')
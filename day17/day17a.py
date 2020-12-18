"""
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole
contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their
super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a
pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z),
there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small
flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.)
state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by
at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2,
the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube
becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains
inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and
determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it.
(In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle
is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state
after the sixth cycle?

Your puzzle answer was 291.
"""
from copy import deepcopy

entries = []
fname = "input.txt"
wname = "stat.txt"
wp = open(wname, 'w')
outerlimit = 50

def num_neighbors_active(coord, universe):
    # coord is a list of three integers [x,y,z]
    active = 0
    x = coord[0]
    y = coord[1]
    z = coord[2]
    for xi in range(-1, 2):
        for yi in range(-1, 2):
            for zi in range(-1, 2):
                try:
                    if universe[x+xi][y+yi][z+zi] == '#':
                        active += 1
                except IndexError:
                    pass
    if universe[x][y][z] == '#':
        active -= 1
    return active


def print_space(universe, file):
    for lz in range(0, len(universe)):
        print(f'Z level = {lz}')
        file.write(f'Z level = {lz}\n')
        for ly in range(0, len(universe)):
            for lx in range(0, len(universe)):
                print(f' {universe[lx][ly][lz]}', end="")
                file.write(f'{universe[lx][ly][lz]}')
            print(f'')
            file.write(f'\n')
        print(f'')
        file.write(f'\n')

space = []
# Seed space
for x in range(0, outerlimit):
    space.append([])
    for y in range(0, outerlimit):
        space[x].append([])
        for z in range(0, outerlimit):
            space[x][y].append('.')

with open(fname, 'r') as fp:
    for line in fp:
        entries.append(line.strip())
print(entries)

mp = int((outerlimit - len(entries[0])) / 2)
xs = ys = mp
zs = int(outerlimit / 2)
print(f'mp = {mp}')

for entry in entries:
    xs = mp
    for bit in entry:
        # print(f'Seeing bit: {bit} going to {xs},{ys},{zs}')
        space[xs][ys][zs] = bit
        xs += 1
    ys += 1

while False:
    sx = int(input('x:'))
    sy = int(input('y:'))
    sz = int(input('z:'))
    if sx < 0:
        break
    print(f'Loc ({sx},{sy},{sz}) is {space[sx][sy][sz]} and has '
          f'{num_neighbors_active([sx, sy, sz], space)} live neighbors')

icount = 0
while icount < 6:
    print(f'Iteration # {icount}')
    newspace = deepcopy(space)
    for z in range(0, outerlimit):
        for y in range(0, outerlimit):
            for x in range(0, outerlimit):
                numneighbors = num_neighbors_active([x, y, z], space)
                if space[x][y][z] == '.' and numneighbors == 3:
                    newspace[x][y][z] = '#'
                elif space[x][y][z] == '#' and (numneighbors == 2 or numneighbors == 3):
                    newspace[x][y][z] = '#'
                else:
                    newspace[x][y][z] = '.'
    space = deepcopy(newspace)
    icount += 1
    print(f'Evolution # {icount} :')
    # wp.write(f'\n\n+---------------+\n | Evolution # {icount} |\n+---------------+\n')
    # print_space(space, wp)

activecount = 0
for surf in space:
    for row in surf:
        activecount += row.count('#')

print('program complete')
print(f'Number of active cells = {activecount}')
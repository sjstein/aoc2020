"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to
take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to
safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help,
you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship
is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the
following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position
and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's
starting position?

Your puzzle answer was 1221.
"""

ship = [90, 0, 0]      # [Facing direction, position east, position north]
directions = ('N', 'S', 'E', 'W', 'F')

entries = []
fname = "input.txt"


def move(cmd, loc):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dir == 'F':
        if loc[0] == 0 or loc[0] == 360:
            dir = 'N'
        elif loc[0] == 90:
            dir = 'E'
        elif loc[0] == 180:
            dir = 'S'
        elif loc[0] == 270:
            dir = 'W'
        else:
            print (f'Error in move command {cmd}')
    if dir == 'N':
        loc[2] += dist
    elif dir == 'S':
        loc[2] -= dist
    elif dir == 'E':
        loc[1] += dist
    elif dir == 'W':
        loc[1] -= dist
    else:
        print(f'Error in function move with cmd: {cmd}')
    return loc


def turndeg(cmd, loc):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dir == 'R':
        loc[0] += dist
    elif dir == 'L':
        loc[0] -= dist
    while loc[0] > 360:
        loc[0] -= 360
    while loc[0] < 0:
        loc[0] += 360
    return loc


with open(fname, 'r') as fp:
    for line in fp:
        entries.append(line.strip())
print(entries)

for command in entries:
    print(f'Ship status : {ship}')
    if command[0] in directions:
        ship = move(command, ship)
    else:
        ship = turndeg(command, ship)

print(f'Program complete - ship info: {ship}')
print(f'Manhattan distance = {abs(ship[1]) + abs(ship[2])}')

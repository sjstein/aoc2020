"""
--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the
back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is,
if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north),
leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship.
The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north),
leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship.
The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south),
leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and
the ship's starting position?

Your puzzle answer was 59435.
"""

ship = ['E', 0, 0]
waypoint = [10, 1]
directions = ('N', 'S', 'E', 'W', 'F')

entries = []
fname = "input.txt"

def move(cmd, loc, way):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dir == 'F':
        for i in range(dist):
            loc[1] += way[0]
            loc[2] += way[1]
    elif dir == 'N':
        way[1] += dist
    elif dir == 'S':
        way[1] -= dist
    elif dir == 'E':
        way[0] += dist
    elif dir == 'W':
        way[0] -= dist
    else:
        print(f'Error in function move with cmd: {cmd}')
    return loc, way


def turn(cmd, loc):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dist == 270:
        if dir == 'R':
            dir = 'L'
        else:
            dir = 'R'
        dist = 90

    x = loc[0]
    y = loc[1]
    if dir == 'R':
        if dist == 90:
            loc[0] = y
            loc[1] = -x
        elif dist == -90:
            loc[0] = -y
            loc[1] = x
        elif dist == 180:
            loc[0] = -x
            loc[1] = -y
        else:
            print(f'Error in function turn with cmd: {cmd}')
    elif dir == 'L':
        if dist == 90:
            loc[0] = -y
            loc[1] = x
        elif dist == -90:
            loc[0] = y
            loc[1] = -x
        elif dist == 180:
            loc[0] = -x
            loc[1] = -y
        else:
            print(f'Error in function turn with cmd: {cmd}')
    return loc


with open(fname, 'r') as fp:
    for line in fp:
        entries.append(line.strip())
print(entries)

for command in entries:
    print(f'Ship status : {ship}')
    if command[0] in directions:
        ship, waypoint = move(command, ship, waypoint)
    else:
        waypoint = turn(command, waypoint)

print(f'Program complete - ship info: {ship}')
print(f'Manhattan distance = {abs(ship[1]) + abs(ship[2])}')

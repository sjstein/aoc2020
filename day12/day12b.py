"""

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
    if command[0] in directions:
        ship, waypoint = move(command, ship, waypoint)
    else:
        waypoint = turn(command, waypoint)

print(f'Program complete - ship info: {ship}')
print(f'Manhattan distance = {abs(ship[1]) + abs(ship[2])}')

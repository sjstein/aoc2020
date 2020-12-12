"""

"""
ship = ['E', 0, 0]
directions = ('N', 'S', 'E', 'W', 'F')

entries = []
fname = "input.txt"

def move(cmd, loc):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dir == 'F':
        dir = loc[0]
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


def turn(cmd, loc):
    dir = cmd[0]
    dist = int(cmd[1:])
    if dist == 270:
        if dir == 'R':
            dir = 'L'
        else:
            dir = 'R'
        dist = 90

    if dir == 'R':
        if dist == 90:
            if loc[0] == 'E':
                loc[0] = 'S'
            elif loc[0] == 'S':
                loc[0] = 'W'
            elif loc[0] == 'W':
                loc[0] = 'N'
            elif loc[0] == 'N':
                loc[0] = 'E'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        elif dist == -90:
            if loc[0] == 'E':
                loc[0] = 'N'
            elif loc[0] == 'S':
                loc[0] = 'E'
            elif loc[0] == 'W':
                loc[0] = 'S'
            elif loc[0] == 'N':
                loc[0] = 'W'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        elif dist == 180:
            if loc[0] == 'E':
                loc[0] = 'W'
            elif loc[0] == 'S':
                loc[0] = 'N'
            elif loc[0] == 'W':
                loc[0] = 'E'
            elif loc[0] == 'N':
                loc[0] = 'S'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        else:
            print(f'Error in function turn with cmd: {cmd}')
    elif dir == 'L':
        if dist == 90:
            if loc[0] == 'E':
                loc[0] = 'N'
            elif loc[0] == 'S':
                loc[0] = 'E'
            elif loc[0] == 'W':
                loc[0] = 'S'
            elif loc[0] == 'N':
                loc[0] = 'W'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        elif dist == -90:
            if loc[0] == 'E':
                loc[0] = 'S'
            elif loc[0] == 'S':
                loc[0] = 'W'
            elif loc[0] == 'W':
                loc[0] = 'N'
            elif loc[0] == 'N':
                loc[0] = 'E'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        elif dist == 180:
            if loc[0] == 'E':
                loc[0] = 'W'
            elif loc[0] == 'S':
                loc[0] = 'N'
            elif loc[0] == 'W':
                loc[0] = 'E'
            elif loc[0] == 'N':
                loc[0] = 'S'
            else:
                print(f'Error in function turn with cmd: {cmd}')
        else:
            print(f'Error in function turn with cmd: {cmd}')
    else:
        print(f'Error in function move with cmd: {cmd}')
    return loc


with open(fname, 'r') as fp:
    for line in fp:
        entries.append(line.strip())
print(entries)

for command in entries:
    if command[0] in directions:
        ship = move(command, ship)
    else:
        ship = turn(command, ship)

print(f'Program complete - ship info: {ship}')
print(f'Manhattan distance = {abs(ship[1]) + abs(ship[2])}')

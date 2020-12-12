"""
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care
about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight
directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an
occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty
seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you
count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached,
how many seats end up occupied?

Your puzzle answer was 1914.
"""


fname = 'input.txt'
rows = []
seats = []
rows2 = []


def check_adjacent(sarr, row, col):
    empties = 0
    free = ['L', '-']
    i = 1
    tl = tp = tr = ml = me = mr = bl = bm = br = 'X'
    while tl not in free and tl != '#':
        tl = sarr[row - i][col - i]
        i += 1
    i = 1
    while tp not in free and tp != '#':
        tp = sarr[row - i][col]
        i += 1
    i = 1
    while tr not in free and tr != '#':
        tr = sarr[row - i][col + i]
        i += 1
    i = 1
    while ml not in free and ml != '#':
        ml = sarr[row][col - i]
        i += 1
    i = 1
    while mr not in free and mr != '#':
        mr = sarr[row][col + i]
        i += 1
    i = 1
    while bl not in free and bl != '#':
        bl = sarr[row + i][col - i]
        i += 1
    i = 1
    while bm not in free and bm != '#':
        bm = sarr[row + i][col]
        i += 1
    i = 1
    while br not in free and br != '#':
        br = sarr[row + i][col + i]
        i += 1

    # print(f'Seat check\n{tl} {tp} {tr}\n{ml} {me} {mr}\n{bl} {bm} {br}')

    if tl in free:
        empties += 1
    if tp in free:
        empties += 1
    if tr in free:
        empties += 1
    if ml in free:
        empties += 1
    if mr in free:
        empties += 1
    if bl in free:
        empties += 1
    if bm in free:
        empties += 1
    if br in free:
        empties += 1

    return empties


def dump_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(f'{map[r][c]}', end='')
        print('')
    return


def free_seats(map):
    count = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 'L':
                count += 1
    return count


def occupied_seats(map):
    count = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == '#':
                count += 1
    return count


with open(fname,'r') as fp:
    for line in fp:
        temp = (line.rstrip())
        for char in temp:
            seats.append(char)
        seats.insert(0, '-')
        seats.append('-')
        rows.append(seats[:])
        seats.clear()

rows.insert(0, '-' * len(rows[0]))
rows.append('-' * len(rows[0]))

lastfree = free_seats(rows)

occlist = []
vaclist = []
numfree = 999
loopcount = 1

dump_map(rows)
while lastfree != numfree:
    lastfree = numfree
    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            adj = check_adjacent(rows, r, c)
            # print(f'Seat ({r},{c}) has {adj} open spots adjacent')
            if rows[r][c] != '#' and rows[r][c] != '.' and adj >= 8:
                occlist.append([r, c])
            elif rows[r][c] == '#' and adj <= 3:
                vaclist.append([r, c])

    for r, c in occlist:
        rows[r][c] = '#'
    for r, c in vaclist:
        rows[r][c] = 'L'
    occlist.clear()
    vaclist.clear()

    numfree = free_seats(rows)
    occupied = occupied_seats(rows)
    loopcount += 1
    print(f'Iteration {loopcount} with {numfree} free seats and {occupied} occupied seats')
    dump_map(rows)
    print('\n')

print(f'program complete after {loopcount} iterations : {occupied_seats(rows)} seats occupied')
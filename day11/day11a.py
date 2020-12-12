"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the
tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry,
you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can
predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
For example, the initial seat layout might look like this:

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

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and
always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from the seat).
The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause
no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?

Your puzzle answer was 2126.
"""
fname = 'test.txt'
rows = []
seats = []
rows2 = []


def check_adjacent(sarr, row, col):
    empties = 0
    free = ['.', 'L', '-']
    tl = sarr[row - 1][col - 1]
    tp = sarr[row - 1][col]
    tr = sarr[row - 1][col + 1]
    ml = sarr[row][col - 1]
    me = sarr[row][col]
    mr = sarr[row][col + 1]
    bl = sarr[row + 1][col - 1]
    bm = sarr[row + 1][col]
    br = sarr[row + 1][col + 1]

    #print(f'Seat check\n{tl} {tp} {tr}\n{ml} {me} {mr}\n{bl} {bm} {br}')

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

while lastfree != numfree:
    lastfree = numfree
    for r in range(1, len(rows) - 1):
        for c in range(1, len(rows[0]) - 1):
            adj = check_adjacent(rows, r, c)
            #print(f'Seat ({r},{c}) has {adj} open spots adjacent')
            if rows[r][c] != '#' and rows[r][c] != '.' and adj >= 8:
                occlist.append([r, c])
            elif rows[r][c] == '#' and adj <= 4:
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
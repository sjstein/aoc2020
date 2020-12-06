"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 711.
"""

import math


def normal_round(n):
    # Added this rounding function as we need to round 1/2 to 1 and python uses "banker's rounding" with the normal
    # round method.
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def find_row(rowstr):
    maxrow = 127
    minrow = 0
    for i in range(7):
        if rowstr[i] == 'B':
            minrow = minrow + normal_round((maxrow - minrow) / 2)
        else:
            maxrow = maxrow - normal_round((maxrow + 1 - minrow) / 2)
        # print(f'iterated in find_row with min: {minrow} and max: {maxrow}')
    return int(minrow)


def find_col(seatstr):
    maxcol = 7
    mincol = 0
    for i in range(3):
        if seatstr[i] == 'R':
            mincol = mincol + normal_round((maxcol - mincol) / 2)
        else:
            maxcol = maxcol - normal_round((maxcol + 1 - mincol) / 2)
        #print(f'{mincol} , {maxcol}')
    return int(mincol)


# Begin main
inputfile = 'input.txt'
fp = open(inputfile, 'r')
highest = 0
sidlist = []

for line in fp:
    head = line[:7]
    tail = line[7:10]
    row = find_row(head)
    col = find_col(tail)
    sid = row * 8 + col
    # print(f'Found sid: {sid} at row: {row} and col: {col}')
    sidlist.append(sid)
    if sid > highest:
        highest = sid

sidlist.sort()
tid = 5
# tid is the current seat id being tested. Starting at 5 since the first 5 ids are n/a as witnessed by examining
# the sorted list of seat ids.
for myid in sidlist:
    if myid - tid > 1:
        print(f'Found seat issue tid: {tid} myid: {myid}')
        print(f'My seat is likely: {normal_round((tid + myid) / 2)}')
    tid = myid
    #print(myid)





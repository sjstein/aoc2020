
"""
--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be
using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder.
Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the
estination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating
bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different, and two of which are floating.
Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are
written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum
of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left
in memory after it completes?

Your puzzle answer was 3260587250457.
"""
import re
fname = "input.txt"


def expand(map, ilist):
    """
    :param map: A list of characters of {0,1,X}
    :param ilist: Input list of permutations generated around (0,1) of X
    :return: n/a - ilist is appended with the int values of the iterated memory locations
    """
    # Map is a list with an arbitrary number of elements that have either a 1, 0, or X
    # For each X in the list, this function will append at iteration into the ilist parameter

    if map.count('X') > 0:
        # Find first X to replace
        bc = 0
        map1 = map[:]
        map2 = map[:]
        for bit in map:
            if bit == 'X':
                map1[bc] = '0'
                map2[bc] = '1'
                expand(map1, ilist)
                expand(map2, ilist)
                break
            bc += 1
    else:
        st = ''
        # ilist.append(st.join(map))
        ilist.append(int(st.join(map), 2))


def maskedaddr(mask, addr):
    place = 0
    mlist = list(mask)
    alist = list(f'{int(addr):036b}')
    retstr = ''
    for c in mlist:
        if c == '1':
            alist[place] = '1'
        elif c == 'X':
            alist[place] = 'X'
        place += 1
    return retstr.join(alist)


memdict = {}
memspace = []   # [addr, contents]
memlist = []

with open(fname, 'r') as fp:
    for line in fp:
        if line.startswith('mask'):
            maskstr = line.strip()[-36:]
            print(f'found mask: {maskstr}')
            # input('press enter')
        else:
            memloc = re.findall('\[(.+?)]', line.strip())[0]
            memval = re.findall('= (.+)', line.strip())[0]
            maskedval = maskedaddr(maskstr, int(memloc))
            print(f'found memory loc: {memloc}')
            print(f'found memory val: {memval}')
            print(f'found masked val: {maskedval}')
            expand(list(maskedval), memlist)
            print(f'List of memory iterations: {memlist}')
            for key in memlist:
                memdict[key] = memval
            memlist.clear()
print(memdict)

for key in memdict:
    memspace.append([int(key), int(memdict[key])])
memspace.sort()
print(memspace)

memtotal = 0
for memloc in memspace:
    print(f'Memory location {memloc[0]} contains {memloc[1]}')
    memtotal += memloc[1]
print(f'program complete with total = {memtotal}')



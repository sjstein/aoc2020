"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found:
you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127.
(Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range;
in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?

Your puzzle answer was 1766397.
"""

fname = 'input.txt'
entries = []
preamble = 25

def test_sum(ent, ep, prelen):
    """
    :param ent: List of all entries
    :param ep: Pointer to current entry being tested
    :param prelen: Length of preamble
    :return: True if ent[val] can be made from len(preamble) entries
    """
    n1 = ep - prelen
    n2 = ep - prelen + 1
    while n1 < len(ent):
        # print(f'testing ent[{n1}] ({ent[n1]}) + ent[{n2}] ({ent[n2]}) = {ent[ep]}?')
        if int(ent[n1]) + int(ent[n2]) == int(ent[ep]):
            return True
        if n2 >= ep - 1:
            n1 += 1
            n2 = ep - prelen
        n2 += 1
        if n1 == n2:
            n2 += 1
    return False


with open(fname, 'r') as fp:
    for line in fp:
        entries.append(int(line.rstrip()))

print(entries)

enum = preamble

while enum < len(entries) - 1:
    if test_sum(entries, enum, preamble):
        print(f'{entries[enum]} returned TRUE')
    else:
        print(f'{entries[enum]} returned FALSE')
        break
    enum += 1

invnum = int(entries[enum])
print(f'Found invalid number: {invnum}\n   looking for summation sequence...')

n1 = 0
n2 = 1
tempsum = int(entries[n1])

#while n1 < len(entries):
while True:
    tempsum += int(entries[n2])
    if tempsum == invnum:
        print(f'Found summation solution: entries[{n1}] = {entries[n1]} and entries[{n2}] = {entries[n2]}')
        print(f'Min value in range = {min(entries[n1:n2+1])}, max value in range = {max(entries[n1:n2+1])}'
              f' Sum = {min(entries[n1:n2+1]) + max(entries[n1:n2+1])}')
        break
    elif tempsum > invnum:
        print(f'Sequence [{n1}:{n2}] invalid. Resetting indices and retrying.')
        n1 += 1
        n2 = n1
        tempsum = int(entries[n1])
    n2 += 1
    if n2 > len(entries)-1:
        n2 = n1 + 1


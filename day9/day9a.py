"""
--- Day 9: Encoding Error ---
With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen
in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips.
Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an
old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two
of the 25 immediately previous numbers. The two numbers will have different values, and there might be more
than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next number
must be the sum of two of those numbers:

26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
49 would be a valid next number, as it is the sum of 24 and 25.
100 would not be valid; no two of the previous 25 numbers sum to 100.
50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair must be
different.
Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20.
Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:

26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
65 would not be valid, as no two of the available numbers sum to it.
64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.
Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):

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
In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers;
the only number that does not follow this rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

Your puzzle answer was 14144619.
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
        entries.append(line.rstrip())

print(entries)

enum = preamble

while enum < len(entries) - 1:
    if test_sum(entries, enum, preamble):
        print(f'{entries[enum]} returned TRUE')
    else:
        print(f'{entries[enum]} returned FALSE')
        break
    enum += 1



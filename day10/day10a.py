"""

"""

fname = 'input.txt'

entries = []

with open(fname, 'r') as fp:
    for line in fp:
        entries.append(int(line.rstrip()))

print(entries)
print(f'Max jolt = {max(entries)}, min jolt = {min(entries)}')
c = 0
j1 = 0 # Source
one = 0
two = 0
three = 0
while c <= len(entries):
    diff = min(entries) - j1
    entries[entries.index(min(entries))] = 9999999999999
    if diff == 1:
        one += 1
    elif diff == 2:
        two += 1
    else:
        three += 1
    c += 1
    j1 += diff

print(f'Test done: {one}, {two}, {three}; product: {one * three}')

"""

"""

entries = []
fname = "input.txt"

with open(fname, 'r') as fp:
    for line in fp:
        entries.append(int(line.strip()))
print(entries)

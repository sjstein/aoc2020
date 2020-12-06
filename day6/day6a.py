"""

"""

# Begin Main
inputfile = 'test.txt'
entcount = 0
entries = [[], []]

fp = open(inputfile, 'r')
print(f'{entries}, sizes = {len(entries)}, {len(entries[entcount])}')
#entries = fp.read().splitlines()
for line in fp:
    print(entries[entcount])
    if line == f'\n' :
        print('blank line')
        entries.append('[], []')
        entcount += 1
    else:
        entries[entcount].append(line.split())


print(entries)




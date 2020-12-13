"""

"""

entries = []
fname = "input.txt"

with open(fname, 'r') as fp:
    entries.append(fp.readline().strip())
    entries.append(fp.readline().strip().split(','))
print(entries)
lowest = 9999999999
lowid = 9999
offsetarr = []
arrtime = int(entries[0])
indx = 0
for t in entries[1]:
    if t <= 'X':
        offsetarr.append([t,indx])
    indx += 1

print(offsetarr)

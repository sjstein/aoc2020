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
tdiffarr = []
arrtime = int(entries[0])
for t in entries[1]:
    if t <= 'X':
        step = int(t)
        accum = 0
        for i in range(step, arrtime + step, step):
            accum += step
            if accum > arrtime:
                tdiffarr.append(step)
                tdiffarr.append(accum)
                if accum - arrtime < lowest:
                    lowest = accum - arrtime
                    lowid = t
                break

print(tdiffarr)
print(f'Lowest value = {lowest} on bus {lowid}')
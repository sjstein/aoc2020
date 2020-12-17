"""

"""
import re

fname = "test.txt"
tickets = []
rulesdict = {}

with open(fname, 'r') as fp:
    line = fp.readline()
    while line != '\n':
        key = re.findall('\A.+: ', line.strip())[0]

        ruleset = ([re.findall(': (.+) or (.+)', line.strip())[0][0],
                      re.findall(': (.+) or (.+)', line.strip())[0][1]])
        n1 = int(re.findall('(.+)-', ruleset[0])[0])
        n2 = int(re.findall('-(.+)', ruleset[0])[0]) + 1
        n3 = int(re.findall('(.+)-', ruleset[1])[0])
        n4 = int(re.findall('-(.+)', ruleset[1])[0]) + 1
        # print(f'Rule ranges: {n1},{n2} and {n3},{n4}')
        rulesdict[key] = [n1, n2, n3, n4]
        line = fp.readline()
    next(fp)
    line = fp.readline()
    myticket = line.strip().split(',')
    next(fp)
    next(fp)
    for line in fp:
        tickets.append(line.strip().split(','))
flat_tix = [int(item) for sublist in tickets for item in sublist]
print(f'Input file parsed with the following:\n'
      f'rules = {rulesdict}\n'
      f'My ticket = {myticket}\n'
      f'Nearby tickets = {tickets}')
# Strip out invalid tickets
tnum = 0
enum = 0
eclass = {}
input('cr')
for ticket in tickets:
    valid = True
    enum = 0
    for entry in ticket:
        for key in rulesdict:
            k1 = rulesdict[key][0]
            k2 = rulesdict[key][1]
            k3 = rulesdict[key][2]
            k4 = rulesdict[key][3]
            if (int(entry) in range(k1, k2) or int(entry) in range(k3, k4)) & (key not in ticket):
                print(f'In here with entry = {entry}, key = {key}')
                if enum not in eclass:
                    eclass[enum] = [key]
                else:
                    eclass[enum].append(key)
        tnum += 1
print(eclass)






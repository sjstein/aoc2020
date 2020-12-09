"""

"""




# Begin Main
inputfile = 'test.txt'
ansfile = 'answers.txt'
entries = []
keys = []
contents = []
nobagphrase = 'contain no other bags.'


with open(inputfile, 'r') as fp:
    for line in fp:
        entries.append(line.rstrip().split(' bags '))
print(f'Entries = {entries}')

for bagname in entries:
    keys.append(bagname[0])
print(f'Bag names = {keys}')

for bagcontents in entries:
    contents.append(bagcontents[1].replace('contain ', '').replace(' bag.', '').replace(' bags.', '')\
                    .replace(' bag', '').replace(' bags', '').replace(', ', ',')\
                    .replace('no other', '').split(','))
print(f'Bag contents = {contents}')

# make dict
bag_dict = dict(zip(keys, contents))
print(f'{bag_dict}')

validbags = []
print('Bag content summary:')
for i in range(len(entries)):
    print(f'{keys[i]} <- {bag_dict[keys[i]]}')

seed = 'shiny gold'
baglist = []





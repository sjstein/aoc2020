"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from
a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same
criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 120637440.
"""

entries = []
x = 0
y = 0
z = 0
esc = False

SOLUTION = 2020

fp = open('input.txt', 'r')

for line in fp:
    entries.append(int(line.strip()))

while x < len(entries):
    y = 0
    while y < len(entries):
        if entries[x] + entries[y] < SOLUTION:
            # Possible to have third value, so iterate again
            z = 0
            while z < len(entries):
                # print(f'Solving in Z at ({x},{y},{z})')
                if entries[x] + entries[y] + entries[z] == SOLUTION:
                    esc = True
                    print(f'Found solution set ({entries[x]},{entries[y]},{entries[z]}) @ ({x},{y},{z})')
                    print(f'Product = {entries[x] * entries[y] * entries[z]}')
                    break
                z += 1
                if esc:
                    break
            y += 1
        else:
            y += 1
    if esc:
        print('Normal termination')
        break
    x += 1
if not esc:
    print('No solution found')


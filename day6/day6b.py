"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which
everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c,
they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

Your puzzle answer was 3392.
"""


def all_answered(group, answer):
    result = True
    for person in group:
        if answer not in person:
            result = False
            break
    return result


def parse_questions(entries):
    result = 0
    for group in entries:        # Each group of answers [list]
         for ans in qlist:       # Each question letter
            result += all_answered(group, ans)
            #print(f'Tested group {group} for ans {ans} result: {all_answered(group, ans)}')
    return result


# Begin Main
inputfile = 'input.txt'
ansfile = 'answers.txt'
entries = []
llist = []

# Populate the list of possible answers using a comma-delimited text file
with open(ansfile, 'r') as fp:
    qlist = fp.read().rstrip().split(',')

with open(inputfile, 'r') as fp:
    for line in fp:
        if line == f'\n' :
            entries.append(llist)
            llist = []
        else:
            llist.append(line.rstrip())
    entries.append(llist)
    # entries has a list of entries organized by groups, so:
    # len(entries) yields number of groups who responded
    # len(entries[x]) yields number of people in group x
    # len(entries[x][y]) yields number of questions answered by person y in group x

print(f'Processed {len(entries)} groups.')



print(f'The answer is: {parse_questions(entries)}')




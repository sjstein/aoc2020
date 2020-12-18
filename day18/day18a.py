"""

"""
import re

expressions = []
fname = "input.txt"

with open(fname, 'r') as fp:
    for line in fp:
        expressions.append(line.strip())

accum = 0
for expression in expressions:
    print(f'Evaluating: {expression}')
    # Check for parenthesis
    while '(' in expression:
        try:
           # sub = re.search('\((\d+ (\+|\*) \d+)+\)', expression).group(0)
            sub = re.search('\((\d|\*|\+|\s)*\)', expression).group(0)
        except AttributeError:
            print(f'Unable to parse {expression} with error: {e}')
        sub1 = sub.replace('(', '')
        sub1 = sub1.replace(')', '')
        sub2 = sub1.split(' ')
        while len(sub2) > 1:
            num1 = sub2[0]
            opr = sub2[1]
            num2 = sub2[2]
            result = None
            if opr == '+':
                result = int(num1) + int(num2)
            elif opr == '*':
                result = int(num1) * int(num2)
            sub2.remove(num1)
            sub2.remove(opr)
            sub2.remove(num2)
            sub2.insert(0, str(result))
        # print(f'Replacing {sub} with {result} in {expression}')
        expression = expression.replace(sub, str(result))
    # So now we should have a non-parenthetical expression
    splitexpr = expression.split(' ')
    while len(splitexpr) > 1:
        num1 = splitexpr[0]
        opr = splitexpr[1]
        num2 = splitexpr[2]
        result = None
        if opr == '+':
            result = int(num1) + int(num2)
        elif opr == '*':
            result = int(num1) * int(num2)
        splitexpr.remove(num1)
        splitexpr.remove(opr)
        splitexpr.remove(num2)
        splitexpr.insert(0, str(result))
        # print(splitexpr)
    accum += int(splitexpr[0])
print(f'program complete with sum: {accum}')




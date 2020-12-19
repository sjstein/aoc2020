"""
--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the
next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?

Your puzzle answer was 88500956630893.
"""
import re

expressions = []
fname = "input.txt"


def reduce(expr):
    result = None
    while len(expr) > 1:
        # Handle addition operation at highest priority (and left-to-right)
        while '+' in expr:
            pindex = expr.index('+')
            num1 = expr[pindex - 1]
            num2 = expr[pindex + 1]
            result = int(num1) + int(num2)
            del expr[pindex - 1:pindex + 2]
            expr.insert(pindex - 1, str(result))
        # Now compute products left-to-right
        if len(expr) > 1:
            num1 = expr[0]
            num2 = expr[2]
            result = int(num1) * int(num2)
            del expr[0:3]
            expr.insert(0, str(result))
    return str(result)


with open(fname, 'r') as fp:
    for line in fp:
        expressions.append(line.strip())

accum = 0
for expression in expressions:
    print(f'Evaluating: {expression}')
    # Check and remove parenthesis (evaluating within)
    while '(' in expression:
        try:
            sub = re.search(r'\((\d|\*|\+|\s)*\)', expression).group(0)
        except AttributeError as e:
            print(f'Unable to parse {expression} with error: {e}')
            exit()
        sub1 = sub.replace('(', '')
        sub1 = sub1.replace(')', '')
        sub2 = sub1.split(' ')
        result = reduce(sub2)
        print(f'Replacing {sub} with {result} in {expression}')
        expression = expression.replace(sub, str(result))
    # So now we should have a non-parenthetical expression
    splitexpr = expression.split(' ')
    accum += int(reduce(splitexpr))
print(f'program complete with sum: {accum}')




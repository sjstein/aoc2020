"""
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted
by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*),
and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before
it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator,
and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the
operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form
 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the
homework; what is the sum of the resulting values?

Your puzzle answer was 13976444272545.
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
            sub = re.search(r'\((\d|\*|\+|\s)*\)', expression).group(0)
        except AttributeError as e:
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




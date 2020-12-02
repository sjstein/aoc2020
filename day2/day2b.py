"""
While it appears you validated the passwords correctly, they don't seem to be what the
Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the
 sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character,
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the
purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was 670.
"""

x = 0
validpassword = 0
inputfile = 'input.txt'

fp = open(inputfile, 'r')
entries = fp.read().splitlines()
# Recall input format is:
# x-y c: <str>
# where (x) and (y) are integers and (c) is a character

while x < len(entries):
    pchar = entries[x].split(': ')[0].split(' ')[1]
    pos1char = int(entries[x].split(': ')[0].split(' ')[0].split('-')[0])
    pos2char = int(entries[x].split(': ')[0].split(' ')[0].split('-')[1])
    pwstring = entries[x].split(': ')[1]
    print(f'Checking {pwstring} for char \'{pchar}\' at position {pos1char} XOR {pos2char} ')
    if (pwstring[pos1char-1] == pchar) != (pwstring[pos2char-1] == pchar):
        print(f'Valid')
        validpassword += 1
    x += 1

print(f'Found {validpassword} valid passwords')

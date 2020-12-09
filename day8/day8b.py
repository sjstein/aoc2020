"""
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
(No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction
in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop,
never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates!
The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last
instruction in the file. With this change, after the program terminates,
the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the
value of the accumulator after the program terminates?

Your puzzle answer was 1036.
"""

ifile = 'input.txt'
program = []
statement = []
acc = 0
pc = 0
pcs = []
lnop = []
ljmp = []


def poplist(prog, cmd):
    """
    :param prog: list containing the program contents [[cmd,arg],...]
    :param cmd: cmd string to search for
    :return: a list of program lines which contain cmd
    """
    c = 0
    flist = []
    while c < len(prog):
        if prog[c][0] == cmd:
            flist.append(c)
        c += 1
    return flist


with open(ifile, 'r') as fp:
    for line in fp:
        parse = line.rstrip().split(' ')
        # parse = ['nop','+0']
        program.append(parse)
print(program)

# Generate list of nops
lnop = poplist(program, 'nop')  # List of line numbers of nop command
ljmp = poplist(program, 'jmp')  # List of line numbers of jmp command
cnop = 0                        # pointer to next nop to be replaced if needed
cjmp = 0                        # pointed to next jmp to be replaced if needed
trynop = True                   # Flag to try replacing nop commands
tryjmp = True                   # Flag to try replacing jmp commands


while pc < len(program):
    cmd = program[pc][0]
    arg = program[pc][1]
    origpc = pc
    # print(f'pc: {pc}, cmd: {cmd}, arg: {arg} acc: {acc}')
    if cmd == 'nop':
        pc += 1
    elif cmd == 'acc':
        if arg[0] == '+':
            acc += int(arg[1:])
            pc += 1
        else:
            acc -= int(arg[1:])
            pc += 1
    elif cmd == 'jmp':
        if arg[0] == '+':
            pc += int(arg[1:])
        else:
            pc -= int(arg[1:])
    else:
        print(f'invalid command: {cmd}')
        break
    if (pc in pcs):
        # Found a looping error - lets see if we can correct
        # print(f'Looping issue at pc: {pc} from {program[origpc]}')
        if trynop:
            if cnop > 0:
                program[lnop[cnop-1]][0] = 'nop'    # Put the previous nop cmd back
            if cnop > len(lnop)-1:
                trynop = False  # All done with replacing nop
            else:
                program[lnop[cnop]][0] = 'jmp'
                cnop += 1
                print(f'changing a nop at {lnop[cnop-1]} to a jmp')
        elif tryjmp:
            if cjmp > 0:
                program[ljmp[cjmp - 1]][0] = 'jmp'  # Put the previous jmp cmd back
            if cjmp > len(ljmp)-1:
                tryjmp = False  # All done with replacing jmp
            else:
                program[ljmp[cjmp]][0] = 'nop'
                cjmp += 1
                print(f'changing a jmp at {ljmp[cjmp-1]} to a nop')
        else:
            print('Unable to fine suitable replacement - exiting')
            break
        # Reset pc and acc to reset to beginning of program
        pc = 0
        acc = 0
        pcs = []
    pcs.append(pc)  # Keep track of program lines executed

print(f'program termination at pc: {pc} with acc: {acc}')

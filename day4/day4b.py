"""
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data
are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules.
Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as
optional. In your batch file, how many passports are valid?

Your puzzle answer was 145.
"""

inputfile = 'input.txt'
validfile = 'valid.txt'
invalidfile = 'invalid.txt'
outputfile = 'day4bOut.txt'
estring = ''
entries = []

fp = open(inputfile, 'r')
wp = open(outputfile, 'w')
wp1 = open(validfile, 'w')
wp2 = open(invalidfile, 'w')


def valid_entry(entry):
    # Function to determine if a given entry is valid in terms of number of fields
    # Returns True if entry if valid, False if not

    if entry.count(':') == 8:
        return True
    if entry.count(':') == 7 and entry.find('cid:') == -1:   # 7 entries and no cid entry
        return True
    return False    # default


def create_dict(records):
    # Function to create a dictionary based on a list of space separated key:value pairs
    # Returns list of dicts

    dictlist = []
    ftuple = []
    for record in records:
        fields = record.split(' ')
        for field in fields:
            ftuple.append((field.split(':')[0], field.split(':')[1]))
        dictlist.append(dict(ftuple))
    return dictlist


def dump_record(record, file):
    # Function to write out contents of record to given file

    file.write(f'byr : {record["byr"]}\n')
    file.write(f'iyr : {record["iyr"]}\n')
    file.write(f'eyr : {record["eyr"]}\n')
    file.write(f'hgt : {record["hgt"]}\n')
    file.write(f'hcl : {record["hcl"]}\n')
    file.write(f'ecl : {record["ecl"]}\n')
    file.write(f'pid : {record["pid"]}\n')
    file.write(f'cid : {record["cid"]}\n')
    file.write(f'------------\n')
    return


# Main program begins
validated = []
invalidated = []
invcount = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0}  # Dict to track invalid entries
recordnum = 0
validpassports = 0
invalidpassports = 0

# Create list of all password entries
for line in fp:
    if len(line) == 1:
        entries.append(estring[:-1])
        estring = ''
    else:
        estring += line.replace('\n', ' ')
entries.append(estring)

print(f'Batch file yielded {len(entries)} entries')

for entry in entries:
    if valid_entry(entry):
        validated.append(entry)
        wp1.write(f'{entry} -- {entry.count(":")} / {entry.find("cid:")}\n')
    else:
        invalidated.append(entry)
        wp2.write(f'{entry} -- {entry.count(":")} / {entry.find("cid:")}\n')

print(f'Valid entries: {len(validated)}, invalid: {len(invalidated)}')

keylist = create_dict(validated)

for key in keylist:
    valid = True

    byr = int(key['byr'])
    iyr = int(key['iyr'])
    eyr = int(key['eyr'])
    hstr = key['hgt']
    hcl = key['hcl']
    ecl = key['ecl']
    pid = key['pid']

    if byr < 1920 or byr > 2002:
        wp.write(f'invalid byr : {byr} (1920-2002)\n')
        invcount['byr'] += 1
        valid = False
    if valid and (iyr < 2010 or iyr > 2020):
        wp.write(f'invalid iyr : {iyr} (2010-2020) \n')
        invcount['iyr'] += 1
        valid = False
    if valid and (eyr < 2020 or eyr > 2030):
        wp.write(f'invalid eyr : {eyr} (2020-2030)\n')
        invcount['eyr'] += 1
        valid = False
    if valid and hstr.endswith('cm'):
        ht = int(hstr.strip('cm'))
        if ht < 150 or ht > 193:
            wp.write(f'Invalid hgt magnitude (150-193cm) : {hstr}\n')
            invcount['hgt'] += 1
            valid = False
    if valid and hstr.endswith('in'):
        ht = int(hstr.strip('in'))
        if ht < 59 or ht > 76:
            wp.write(f'Invalid hgt magnitude (59-76in) : {hstr}\n')
            invcount['hgt'] += 1
            valid = False
    if valid and not (hstr.endswith('in') or hstr.endswith('cm')):
        wp.write(f'Invalid hgt unit : {hstr}\n')
        invcount['hgt'] += 1
        valid = False
    if valid and (len(hcl) != 7 or hcl[0] != '#'):
        wp.write(f'Invalid hcl : {hcl}\n')
        invcount['hcl'] += 1
        valid = False
    if valid and len(ecl) != 3:
        wp.write(f'Invalid ecl (len) : {ecl}\n')
        invcount['ecl'] += 1
        valid = False
    if valid and ecl != 'amb' and ecl != 'blu' and ecl != 'brn' and ecl != 'gry' and ecl != 'grn' and ecl != 'hzl' and\
            ecl != 'oth':
        wp.write(f'Invalid ecl : {ecl}\n')
        invcount['ecl'] += 1
        valid = False
    if valid and len(pid) != 9:
        wp.write(f'Invalid pid : {pid}\n')
        invcount['pid'] += 1
        valid = False
    if valid:
        validpassports += 1
    else:
        dump_record(key, wp)
        invalidpassports += 1
    recordnum += 1

print(f'Program execution complete after processing {recordnum} records.')
print(f'Found {validpassports} valid passports')
print(f'{invalidpassports} invalid passports summarized as:')
print(f'{invcount["byr"]:03d} invalid birth year   [byr]')
print(f'{invcount["iyr"]:03d} invalid issued year  [iyr]')
print(f'{invcount["eyr"]:03d} invalid expired year [eyr]')
print(f'{invcount["hgt"]:03d} invalid height value [hgt]')
print(f'{invcount["hcl"]:03d} invalid hair color   [hcl]')
print(f'{invcount["ecl"]:03d} invalid eye color    [hcl]')
print(f'{invcount["pid"]:03d} invalid passport id  [pid]')





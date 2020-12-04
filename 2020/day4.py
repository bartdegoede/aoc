import re
import string

with open('day4.txt', 'r') as f:
    passports = [passport.strip() for passport in f.read().split('\n\n')]

def validate_basic(passport):
    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    valid_passport = True
    for required_field in required_fields:
        if required_field not in passport:
            valid_passport = False
    return valid_passport

def validate_height(height):
    if height.endswith('cm'):
        return 150 <= int(height.replace('cm', '')) <= 193
    elif height.endswith('in'):
        return 59 <= int(height.replace('in', '')) <= 76
    return False

def validate_hcl(hcl):
    if not hcl.startswith('#'):
        return False
    if not len(hcl) == 7:
        return False
    if not all(c in string.hexdigits for c in hcl[1:]):
        return False
    return True

def validate_passport(passport):
    required_fields = {
        'byr': lambda byr: 1920 <= int(byr) <= 2002,
        'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
        'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
        'hgt': lambda hgt: validate_height(hgt),
        'ecl': lambda ecl: ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda pid: pid.isdigit() and len(pid) == 9,
        'hcl': lambda hcl: validate_hcl(hcl)
    }
    for field, validation in required_fields.items():
        value = re.search(f'{field}:(?P<value>.*?)(\s|$)', passport)
        if value:
            if not validation(value.group('value')):
                return False
        else:
            return False
    return True

valid_passports1 = 0
valid_passports2 = 0
for passport in passports:
    if validate_basic(passport):
        valid_passports1 += 1
    if validate_passport(passport.replace('\n', ' ')):
        valid_passports2 += 1

print(f'There are {valid_passports1} valid passports')
print(f'There are {valid_passports2} valid passports')

#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0

    thousands = {'M': 1000,
                 'MM': 2000,
                 'MMM': 3000}
    hundreds = {'C': 100,
                'CC': 200,
                'CCC': 300,
                'CD': 400,
                'D': 500,
                'DC': 600,
                'DCC': 700,
                'DCCC': 800,
                'CM': 900}
    tens = {'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90}
    units = {'I': 1,
             'II': 2,
             'III': 3,
             'IV': 4,
             'V': 5,
             'VI': 6,
             'VII': 7,
             'VIII': 8,
             'IX': 9}
    convert = [thousands, hundreds, tens, units]
    start = 0
    finnish = 0
    roman_int = found = 0  # found will help us to check the previous sum
    if len(roman_string) - start >= 4:
        finnish += 4
    else:
        finnish += len(roman_string) - start

    while start < len(roman_string):
        section = roman_string[start: finnish]
        for dict in convert:
            if section in list(dict.keys()):
                roman_int += dict[section]
                start = finnish
                if len(roman_string) - start >= 4:
                    finnish += 4
                else:
                    finnish += len(roman_string) - start
                break
        if found == roman_int:  # checks if it found a value of section
            finnish -= 1
        else:
            found = roman_int
            continue

    return roman_int

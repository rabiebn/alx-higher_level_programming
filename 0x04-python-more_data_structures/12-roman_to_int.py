#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0

    thousands = {'M': 1000,
            'MM': 2000,
            'MMM': 3000
            }
    hundreds = {'C': 100,
            'CC': 200,
            'CCC': 300,
            'CD': 400,
            'D': 500,
            'DC': 600,
            'DCC': 700,
            'DCCC': 800,
            'CM': 900
            }
    tens = {'X': 10,
            'XX': 20,
            'XXX':30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90
            }
    units = {'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9
            }
    roman_int = 0
    rev_roman = roman_string[::-1]
    idx = 0 
    while idx < len(roman_string):
        if (len(roman_string) - idx) < 4:
            idx = len(roman_string)
        else:
            idx += 4
        section = rev_roman[:idx]

        if section in list(units.keys()):
            roman_int += units[section]
        elif section in list(tens.keys()):
            roman_int += tens[section]
        elif section in list(hundreds.keys()):
            roman_int += hundreds[section]
        elif section in list(thousands.keys()):
            roman_int += thousands[section]
        else:
            idx -= 1
            continue

    return roman_int

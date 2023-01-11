import re

def string_calculator(string):
    if string == '':
        total = 0
    else:
        total = 0
        splittedString = string.split(',')
        for i in splittedString:
            total += int(i)
    return total
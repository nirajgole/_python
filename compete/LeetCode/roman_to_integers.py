import re
# class Solution:


def romanToInt(s: str) -> int:
    roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
             'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    return sum(map(lambda x: roman[x], re.findall('CM|CD|XC|XL|IX|IV|\w', s)))


print(romanToInt('MCMXCIV'))

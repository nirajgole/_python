# library to import regular expression
import re

# compile if you want to use the same pattern later on, it's faster
pattern = re.compile(r'\d+')

# search will return a match object, if there is no match it will return None
res = pattern.search('123')

# Example 1
# def extract_phone_number(text):
#     pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
#     match = pattern.search(text)
#     if match:
#         return match.group()
#     else:
#         return None

# print(extract_phone_number('My number is 415-555-4242.'))
# print(extract_phone_number('My number is 555-4242.'))

# Example 2
# def extract_all_phone_numbers(text):
#     pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
#     return pattern.findall(text)

# print(extract_all_phone_numbers('My number is 415-555-4242. Call me tomorrow at 415-555-9999'))
# print(extract_all_phone_numbers('My number is 555-4242. Call me tomorrow at 555-9999'))

# Example 3
# def is_valid_phone_number(text):
#     # pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
#     pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#     # fullMatch is a special method that returns True if the pattern matches the entire string
#     #* It's same as adding ^ at the beginning of the pattern and $ at the end of the pattern
#     match = pattern.fullmatch(text)
#     if match:
#         return True
#     return False

# print(is_valid_phone_number('415-555-4242'))
# print(is_valid_phone_number('555-4242'))

# Example 4 URL PARSING
# url_regex = re.compile(r'(https?)://(www\.)?(\w+)(\.\w+)/(\S+)*')
# match = url_regex.search('https://www.google.com/search/asd/asd/asd')
# # group method will return the matched string
# print(f'Protocol: {match.group(0)}')
# print(f'Domain: {match.group(1)}')
# print(f'Everything else: {match.group(2)}')
# print(f'Everything else: {match.group(3)}')
# print(f'Everything else: {match.group(4)}')
# print(f'Everything else: {match.group(5)}')

# groups method will return a tuple of all the matched strings
# print(match.groups())

# Example 5 symbolic groups

# def parse_name(text):
#     name_regex = re.compile(
#         r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.) (?P<first>\w+) (\w+)$')
#     # here ?P<first> is a named group, it will be used to extract the first name
#     matches = name_regex.search(text)
#     print(matches.group('first'))

# parse_name('Mr. John Smith')

# Example 6 Flags
# pattern = re.compile(r"""
# 	^([a-z0-9_\.-]+)	#first part of email
# 	@					#single @ sign
# 	([0-9a-z\.-]+)		#email provider
# 	\.					#single period
# 	([a-z\.]{2,6})$		#com, org, net, etc.
# """, re.X | re.I)
# #Here X is the flag that allows for verbose regular expressions
# #Here I is the flag that allows for case-insensitive matching
# match = pattern.search("ThomaS123@Yahoo.com")
# print(match.group())
# print(match.groups())

#Example 7
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)

    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)

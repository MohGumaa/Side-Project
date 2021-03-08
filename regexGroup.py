#! python3
# regexGroup.py will create group of result for regular expressions
# will help of group function

import re

message = 'My number is 415-555-4242'

# Create regular expression to find phone number and put in group
isPhoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
result = isPhoneNumber.search(message)

# print(f'Phone number found: {result.groups()}')

# print(f'Phone number found: {result.group(1)}')

# print(f'Phone number found: {result.group(2)}')

# print(f'Phone number found: {result.group()}')

# print(f'Phone number found: {result.group(0)}')

# We can destructe the result into variables
areaCode, mainNumber = result.groups()
# print(areaCode)


# Pipe we can use in anywhere you want to match one of many expressions

heroRegex = re.compile(r'Batman|Tina Fey')
match = heroRegex.search('Batman and Tina Fey')
# print(match.group())

match = heroRegex.search('Tina Fey beat Batman')
print(match.group())

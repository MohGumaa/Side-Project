#!python3
# regPattern.py Find phone number in text

import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo= phoneNumberRegex.search('Hello 444-555-2123')
print(mo)
print(mo.group())

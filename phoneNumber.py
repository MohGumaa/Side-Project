#!python3
# phoneNumber.py checkout the pattern format of the text
# if is it match form

'''
    Function use to check if the phone number text match the format
    of 415-555-4242.
'''

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for number in text[0:3]:
        if not number.isdecimal():
            return False

    if text[3] != "-":
        return False

    for number in text[4:7]:
        if not number.isdecimal():
            return False

    if text[7] != "-":
        return False

    for number in text[8:]:
        if not number.isdecimal():

            return False

    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))

print('434131232 is a phone number:')
print(isPhoneNumber('434131232'))

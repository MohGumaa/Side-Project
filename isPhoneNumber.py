#! python3
# isPhoneNumber.py use to find phone number in any text

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for value in text[ : 3]:
        if not value.isdecimal():
            return False
    if text[3] != '-':
        return False

    for value in text[4:7]:
        if not value.isdecimal():
            return False
    if text[7] != '-':
        return False

    for value in text[8: ]:
        if not value.isdecimal():
            return False

    return True



message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

Loop through message and extra phone number
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone Number found: {chunk}")

print("Done")


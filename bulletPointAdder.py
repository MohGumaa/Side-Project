#! python3
# bulletPointAdder.py Add Wikipedia bullet points to start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
list_s = text.split('\n')



# Loop through list of string and append * in begin
str_list = ['* '+ line for line in list_s]

pyperclip.copy(''.join(str_list))


# text = '* ' + text
# print(text.replace('\n', '* '))


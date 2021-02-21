message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# Count number of occureences of each letter in string
for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)

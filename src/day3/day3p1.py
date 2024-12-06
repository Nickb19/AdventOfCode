import re

regex = r"mul\(\d+,\d+\)"
textfile = open('reginp.txt', 'r', re.M)
filetext = textfile.read()
textfile.close()
matches = re.findall(regex, filetext)
total = 0
for match in matches:
    newRegex = r"\d+,\d+"
    numberMatch = re.search(newRegex, match)
    numbers = numberMatch.group().split(',')
    multiply = int(numbers[0]) * int(numbers[1])
    total += multiply
print(total)

import re

regexNNN = r"do\(\).*?mul\(\d+,\d+\).*?don\'t\(\)|do\(\).*?mul\(\d+,\d+\).*$"
regex = r"^mul\(\d+,\d+\).*?don\'t\(\)"

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

goodMatches = re.findall(regexNNN, filetext)
goodTotal = 0

for match in goodMatches:
    newRegex = r"mul\(\d+,\d+\)"
    numberMatch = re.findall(newRegex, match)
    for number in numberMatch:
        numberRegex = r"\d+,\d+"
        numberFind = re.search(numberRegex, number)
        numbers = numberFind.group().split(',')

        multiply = int(numbers[0]) * int(numbers[1])
        goodTotal += multiply


print(goodTotal + total)

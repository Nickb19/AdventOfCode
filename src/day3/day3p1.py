import re

regex = r"/mul\(\d+,\d+\)/gm"
textfile = open('reginp.txt', 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall(regex, filetext)
print(matches)
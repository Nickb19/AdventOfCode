
safe = 0
with open('input.txt') as f:
  lines = f.readlines()
  increasing = True
  for line in lines:
    chars = line.split((' '))
    isSafe = True
    for char in range(len(chars) - 1):
      char1 = int(chars[char])
      char2 = int(chars[char + 1])
      if char1 > char2:
        difference = char1 - char2
      else:
        difference = char2 -char1
      if (difference > 3 or difference < 1):
        isSafe=False
        break
      if char == 0:
        if char1 > char2:
          increasing = False
        else: 
          increasing = True
      if char1 > char2 and increasing is True:
        isSafe=False
        break
      elif char2 > char1 and increasing is False:
        isSafe=False
        break
    if isSafe:
      safe+=1

print(safe)